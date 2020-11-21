#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class TimelineStat:
    def __init__(self):
        resolve = app.GetResolve()
        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        self.tm = project.GetCurrentTimeline()
        self.tm_name = self.tm.GetName()
        self.frame_rate = float(project.GetSetting("timelineFrameRate"))
        self.track_type = "video"
        self.total_duration = 0
        self.total_shots = 0
        self.shots = []

    def process(self):
        track_count = int(self.tm.GetTrackCount(self.track_type))
        for index in range (1, track_count + 1):
            clips = self.tm.GetItemListInTrack(self.track_type, index)
            self.total_shots = len(clips)
            shot_id = 0
            for clip in clips:
                name = clip.GetName()
                duration =  clip.GetDuration() / self.frame_rate
                self.total_duration += duration
                shot_id += 1
                self.shots.append({"shot_id": shot_id, "shot_duration": duration, "name": name})

    def show(self):
       res = {}
       res["timeline_name"] = self.tm_name
       res["frame_rate"] = self.frame_rate
       res["total_shots"] = self.total_shots
       res["total_duration"] = self.total_duration
       res["shots"] = self.shots
       return json.dumps(res, indent=2, sort_keys=True)

tl_stat = TimelineStat()
tl_stat.process()
print("\n\n\n")
print(tl_stat.show())
