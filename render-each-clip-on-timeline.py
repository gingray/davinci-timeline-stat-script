#!/usr/bin/python
# -*- coding: utf-8 -*-
import time


class RenderEachClipOnTimeline:
    def __init__(self):
        resolve = app.GetResolve()
        self.projectManager = resolve.GetProjectManager()
        self.project = self.projectManager.GetCurrentProject()
        # self.t = project.GetTimelineCount()

    def process(self):
        print "Render each clip start"
        time_lines_count = self.project.GetTimelineCount()
        working_timeline = None
        time_line_name = "render_each"
        print "Start looking timeline with name: " + time_line_name

        for index in range(1, time_lines_count + 1):
            timeline = self.project.GetTimelineByIndex(index)
            if timeline.GetName() == time_line_name:
                working_timeline = timeline
                break

        if working_timeline is None:
            print "Timeline not found exit"
            return

        print "Set timeline as current"
        self.project.SetCurrentTimeline(working_timeline)
        timeline_clips = working_timeline.GetItemsInTrack("video", 1)
        print "clips on timeline {}".format(len(timeline_clips))

        render_array_of_clips = []

        for key, clip in timeline_clips.items():
            clip_start = clip.GetStart()
            clip_end = clip.GetEnd()
            clip_name = clip.GetName()
            clip_duration = clip.GetDuration()
            print "name: {}".format(clip_name)
            print "Timeline Start: {}".format(working_timeline.GetStartFrame())
            print "StartFrame: {}".format(clip_start)
            print "EndFrame: {}".format(clip_end)
            print "Duration: {}".format(clip_duration)
            print "-----"
            render_array_of_clips.append({"MarkIn": clip_start, "MarkOut": clip_end, "CustomName": clip_name})

        print "render formats: {}".format(self.project.GetRenderFormats())
        print "render codec: {}".format(self.project.GetRenderCodecs("mp4"))
        self.project.SetCurrentRenderFormatAndCodec("mp4", "H264")

        for item in render_array_of_clips:
            self.project.SetRenderSettings(item)
            self.project.AddRenderJob()
        self.project.StartRendering()

        while self.project.IsRenderingInProgress():
            render_jobs = self.project.GetRenderJobs()
            # print "render jobs: {}".format(render_jobs)
            for key, val in render_jobs.items():
                status = self.project.GetRenderJobStatus(key)
                print "render job status: {}".format(status)
            time.sleep(2)


render = RenderEachClipOnTimeline()
render.process()
print "finish"
