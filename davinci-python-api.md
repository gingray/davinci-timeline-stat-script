SERVICES
DOCUMENTS
Untitled Document.md
Untitled Document.md
PREVIEW AS 
EXPORT AS 
SAVE TO 
IMPORT FROM 
DOCUMENT NAME
Untitled Document.md
MARKDOWNPREVIEWToggle Mode
  
<h2 class="code-line" data-line-start=0 data-line-end=2 ><a id="Updated_as_of_20_October_2020_0"></a>Updated as of 20 October 2020</h2>
<p class="has-line-data" data-line-start="2" data-line-end="4">In this package, you will find a brief introduction to the Scripting API for DaVinci Resolve Studio. Apart from this README.txt file, this package contains folders containing the basic import<br>
modules for scripting access (<a href="http://DaVinciResolve.py">DaVinciResolve.py</a>) and some representative examples.</p>
<p class="has-line-data" data-line-start="5" data-line-end="6">From v16.2.0 onwards, the nodeIndex parameters accepted by SetLUT() and SetCDL() are 1-based instead of 0-based, i.e. 1 &lt;= nodeIndex &lt;= total number of nodes.</p>
<h2 class="code-line" data-line-start=8 data-line-end=10 ><a id="Overview_8"></a>Overview</h2>
<p class="has-line-data" data-line-start="10" data-line-end="13">As with Blackmagic Design Fusion scripts, user scripts written in Lua and Python programming languages are supported. By default, scripts can be invoked from the Console window in the Fusion page,<br>
or via command line. This permission can be changed in Resolve Preferences, to be only from Console, or to be invoked from the local network. Please be aware of the security implications when<br>
allowing scripting access from outside of the Resolve application.</p>
<h2 class="code-line" data-line-start=15 data-line-end=17 ><a id="Prerequisites_15"></a>Prerequisites</h2>
<p class="has-line-data" data-line-start="17" data-line-end="18">DaVinci Resolve scripting requires one of the following to be installed (for all users):</p>
<pre><code>Lua 5.1
Python 2.7 64-bit
Python 3.6 64-bit
</code></pre>
<h2 class="code-line" data-line-start=24 data-line-end=26 ><a id="Using_a_script_24"></a>Using a script</h2>
<p class="has-line-data" data-line-start="26" data-line-end="27">DaVinci Resolve needs to be running for a script to be invoked.</p>
<p class="has-line-data" data-line-start="28" data-line-end="30">For a Resolve script to be executed from an external folder, the script needs to know of the API location.<br>
You may need to set the these environment variables to allow for your Python installation to pick up the appropriate dependencies as shown below:</p>
<pre><code>Mac OS X:
RESOLVE_SCRIPT_API=&quot;/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting&quot;
RESOLVE_SCRIPT_LIB=&quot;/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so&quot;
PYTHONPATH=&quot;$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/&quot;

Windows:
RESOLVE_SCRIPT_API=&quot;%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting&quot;
RESOLVE_SCRIPT_LIB=&quot;C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll&quot;
PYTHONPATH=&quot;%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\&quot;

Linux:
RESOLVE_SCRIPT_API=&quot;/opt/resolve/Developer/Scripting&quot;
RESOLVE_SCRIPT_LIB=&quot;/opt/resolve/libs/Fusion/fusionscript.so&quot;
PYTHONPATH=&quot;$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/&quot;
(Note: For standard ISO Linux installations, the path above may need to be modified to refer to /home/resolve instead of /opt/resolve)
</code></pre>
<p class="has-line-data" data-line-start="47" data-line-end="48">As with Fusion scripts, Resolve scripts can also be invoked via the menu and the Console.</p>
<p class="has-line-data" data-line-start="49" data-line-end="61">On startup, DaVinci Resolve scans the subfolders in the directories shown below and enumerates the scripts found in the Workspace application menu under Scripts.<br>
Place your script under Utility to be listed in all pages, under Comp or Tool to be available in the Fusion page or under folders for individual pages (Edit, Color or Deliver). Scripts under Deliver are additionally listed under render jobs.<br>
Placing your script here and invoking it from the menu is the easiest way to use scripts.<br>
Mac OS X:<br>
- All users: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts<br>
- Specific user:  /Users/&lt;UserName&gt;/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts<br>
Windows:<br>
- All users: %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts<br>
- Specific user: %APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts<br>
Linux:<br>
- All users: /opt/resolve/Fusion/Scripts  (or /home/resolve/Fusion/Scripts/ depending on installation)<br>
- Specific user: $HOME/.local/share/DaVinciResolve/Fusion/Scripts</p>
<p class="has-line-data" data-line-start="62" data-line-end="64">The interactive Console window allows for an easy way to execute simple scripting commands, to query or modify properties, and to test scripts. The console accepts commands in Python 2.7, Python 3.6<br>
and Lua and evaluates and executes them immediately. For more information on how to use the Console, please refer to the DaVinci Resolve User Manual.</p>
<p class="has-line-data" data-line-start="65" data-line-end="72">This example Python script creates a simple project:<br>
#!/usr/bin/env python<br>
import DaVinciResolveScript as dvr_script<br>
resolve = dvr_script.scriptapp(“Resolve”)<br>
fusion = resolve.Fusion()<br>
projectManager = resolve.GetProjectManager()<br>
projectManager.CreateProject(“Hello World”)</p>
<p class="has-line-data" data-line-start="73" data-line-end="75">The resolve object is the fundamental starting point for scripting via Resolve. As a native object, it can be inspected for further scriptable properties - using table iteration and “getmetatable”<br>
in Lua and dir, help etc in Python (among other methods). A notable scriptable object above is fusion - it allows access to all existing Fusion scripting functionality.</p>
<h2 class="code-line" data-line-start=77 data-line-end=79 ><a id="Running_DaVinci_Resolve_in_headless_mode_77"></a>Running DaVinci Resolve in headless mode</h2>
<p class="has-line-data" data-line-start="79" data-line-end="81">DaVinci Resolve can be launched in a headless mode without the user interface using the -nogui command line option. When DaVinci Resolve is launched using this option, the user interface is disabled.<br>
However, the various scripting APIs will continue to work as expected.</p>
<h2 class="code-line" data-line-start=83 data-line-end=85 ><a id="Basic_Resolve_API_83"></a>Basic Resolve API</h2>
<p class="has-line-data" data-line-start="85" data-line-end="86">Some commonly used API functions are described below (*). As with the resolve object, each object is inspectable for properties and functions.</p>
<p class="has-line-data" data-line-start="87" data-line-end="95">Resolve<br>
Fusion()                                        --&gt; Fusion             # Returns the Fusion object. Starting point for Fusion scripts.<br>
GetMediaStorage()                               --&gt; MediaStorage       # Returns the media storage object to query and act on media locations.<br>
GetProjectManager()                             --&gt; ProjectManager     # Returns the project manager object for currently open database.<br>
OpenPage(pageName)                              --&gt; None               # Switches to indicated page in DaVinci Resolve. Input can be one of (“media”, “cut”, “edit”, “fusion”, “color”, “fairlight”, “deliver”).<br>
GetProductName()                                --&gt; string             # Returns product name.<br>
GetVersion()                                    --&gt; [version fields]   # Returns list of product version fields in [major, minor, patch, build, suffix] format.<br>
GetVersionString()                              --&gt; string             # Returns product version in “major.minor.patch[suffix].build” format.</p>
<p class="has-line-data" data-line-start="96" data-line-end="120">ProjectManager<br>
CreateProject(projectName)                      --&gt; Project            # Creates and returns a project if projectName (string) is unique, and None if it is not.<br>
DeleteProject(projectName)                      --&gt; Bool               # Delete project in the current folder if not currently loaded<br>
LoadProject(projectName)                        --&gt; Project            # Loads and returns the project with name = projectName (string) if there is a match found, and None if there is no matching Project.<br>
GetCurrentProject()                             --&gt; Project            # Returns the currently loaded Resolve project.<br>
SaveProject()                                   --&gt; Bool               # Saves the currently loaded project with its own name. Returns True if successful.<br>
CloseProject(project)                           --&gt; Bool               # Closes the specified project without saving.<br>
CreateFolder(folderName)                        --&gt; Bool               # Creates a folder if folderName (string) is unique.<br>
DeleteFolder(folderName)                        --&gt; Bool               # Deletes the specified folder if it exists. Returns True in case of success.<br>
GetProjectListInCurrentFolder()                 --&gt; [project names…] # Returns a list of project names in current folder.<br>
GetFolderListInCurrentFolder()                  --&gt; [folder names…]  # Returns a list of folder names in current folder.<br>
GotoRootFolder()                                --&gt; Bool               # Opens root folder in database.<br>
GotoParentFolder()                              --&gt; Bool               # Opens parent folder of current folder in database if current folder has parent.<br>
GetCurrentFolder()                              --&gt; string             # Returns the current folder name.<br>
OpenFolder(folderName)                          --&gt; Bool               # Opens folder under given name.<br>
ImportProject(filePath)                         --&gt; Bool               # Imports a project from the file path provided. Returns True if successful.<br>
ExportProject(projectName, filePath, withStillsAndLUTs=True) --&gt; Bool  # Exports project to provided file path, including stills and LUTs if withStillsAndLUTs is True (enabled by default). Returns True in case of success.<br>
RestoreProject(filePath)                        --&gt; Bool               # Restores a project from the file path provided. Returns True if successful.<br>
GetCurrentDatabase()                            --&gt; {dbInfo}           # Returns a dictionary (with keys ‘DbType’, ‘DbName’ and optional ‘IpAddress’) corresponding to the current database connection<br>
GetDatabaseList()                               --&gt; [{dbInfo}]         # Returns a list of dictionary items (with keys ‘DbType’, ‘DbName’ and optional ‘IpAddress’) corresponding to all the databases added to Resolve<br>
SetCurrentDatabase({dbInfo})                    --&gt; Bool               # Switches current database connection to the database specified by the keys below, and closes any open project.<br>
# ‘DbType’: ‘Disk’ or ‘PostgreSQL’ (string)<br>
# ‘DbName’: database name (string)<br>
# ‘IpAddress’: IP address of the PostgreSQL server (string, optional key - defaults to ‘127.0.0.1’)</p>
<p class="has-line-data" data-line-start="121" data-line-end="178">Project<br>
GetMediaPool()                                  --&gt; MediaPool          # Returns the Media Pool object.<br>
GetTimelineCount()                              --&gt; int                # Returns the number of timelines currently present in the project.<br>
GetTimelineByIndex(idx)                         --&gt; Timeline           # Returns timeline at the given index, 1 &lt;= idx &lt;= project.GetTimelineCount()<br>
GetCurrentTimeline()                            --&gt; Timeline           # Returns the currently loaded timeline.<br>
SetCurrentTimeline(timeline)                    --&gt; Bool               # Sets given timeline as current timeline for the project. Returns True if successful.<br>
GetName()                                       --&gt; string             # Returns project name.<br>
SetName(projectName)                            --&gt; Bool               # Sets project name if given projectname (string) is unique.<br>
GetPresetList()                                 --&gt; [presets…]       # Returns a list of presets and their information.<br>
SetPreset(presetName)                           --&gt; Bool               # Sets preset by given presetName (string) into project.<br>
AddRenderJob()                                  --&gt; string             # Adds a render job based on current render settings to the render queue. Returns a unique job id (string) for the new render job.<br>
DeleteRenderJob(jobId)                          --&gt; Bool               # Deletes render job for input job id (string).<br>
DeleteAllRenderJobs()                           --&gt; Bool               # Deletes all render jobs in the queue.<br>
GetRenderJobList()                              --&gt; [render jobs…]   # Returns a list of render jobs and their information.<br>
GetRenderPresetList()                           --&gt; [presets…]       # Returns a list of render presets and their information.<br>
StartRendering(jobId1, jobId2, …)             --&gt; Bool               # Starts rendering jobs indicated by the input job ids.<br>
StartRendering([jobIds…], isInteractiveMode=False)    --&gt; Bool       # Starts rendering jobs indicated by the input job ids.<br>
# The optional “isInteractiveMode”, when set, enables error feedback in the UI during rendering.<br>
StartRendering(isInteractiveMode=False)                 --&gt; Bool       # Starts rendering all queued render jobs.<br>
# The optional “isInteractiveMode”, when set, enables error feedback in the UI during rendering.<br>
StopRendering()                                 --&gt; None               # Stops any current render processes.<br>
IsRenderingInProgress()                         --&gt; Bool               # Returns True if rendering is in progress.<br>
LoadRenderPreset(presetName)                    --&gt; Bool               # Sets a preset as current preset for rendering if presetName (string) exists.<br>
SaveAsNewRenderPreset(presetName)               --&gt; Bool               # Creates new render preset by given name if presetName(string) is unique.<br>
SetRenderSettings({settings})                   --&gt; Bool               # Sets given settings for rendering. Settings is a dict, with support for the keys:<br>
# “SelectAllFrames”: Bool<br>
# “MarkIn”: int<br>
# “MarkOut”: int<br>
# “TargetDir”: string<br>
# “CustomName”: string<br>
# “UniqueFilenameStyle”: 0 - Prefix, 1 - Suffix.<br>
# “ExportVideo”: Bool<br>
# “ExportAudio”: Bool<br>
# “FormatWidth”: int<br>
# “FormatHeight”: int<br>
# “FrameRate”: float (examples: 23.976, 24)<br>
# “PixelAspectRatio”: string (for SD resolution: “16_9” or “4_3”) (other resolutions: “square” or “cinemascope”)<br>
# “VideoQuality” possible values for current codec (if applicable):<br>
#    0 (int) - will set quality to automatic<br>
#    [1 -&gt; MAX] (int) - will set input bit rate<br>
#    [“Least”, “Low”, “Medium”, “High”, “Best”] (String) - will set input quality level<br>
# “AudioCodec”: string (example: “aac”)<br>
# “AudioBitDepth”: int<br>
# “AudioSampleRate”: int<br>
# “ColorSpaceTag” : string (example: “Same as Project”, “AstroDesign”)<br>
# “GammaTag” : string (example: “Same as Project”, “ACEScct”)<br>
GetRenderJobStatus(jobId)                       --&gt; {status info}      # Returns a dict with job status and completion percentage of the job by given jobId (string).<br>
GetSetting(settingName)                         --&gt; string             # Returns value of project setting (indicated by settingName, string). Check the section below for more information.<br>
SetSetting(settingName, settingValue)           --&gt; Bool               # Sets the project setting (indicated by settingName, string) to the value (settingValue, string). Check the section below for more information.<br>
GetRenderFormats()                              --&gt; {render formats…} # Returns a dict (format -&gt; file extension) of available render formats.<br>
GetRenderCodecs(renderFormat)                   --&gt; {render codecs…} # Returns a dict (codec description -&gt; codec name) of available codecs for given render format (string).<br>
GetCurrentRenderFormatAndCodec()                --&gt; {format, codec}    # Returns a dict with currently selected format ‘format’ and render codec ‘codec’.<br>
SetCurrentRenderFormatAndCodec(format, codec)   --&gt; Bool               # Sets given render format (string) and render codec (string) as options for rendering.<br>
GetCurrentRenderMode()                          --&gt; int                # Returns the render mode: 0 - Individual clips, 1 - Single clip.<br>
SetCurrentRenderMode(renderMode)                --&gt; Bool               # Sets the render mode. Specify renderMode = 0 for Individual clips, 1 for Single clip.<br>
GetRenderResolutions(format, codec)             --&gt; [{Resolution}]     # Returns list of resolutions applicable for the given render format (string) and render codec (string). Returns full list of resolutions if no argument is provided. Each element in the list is a dictionary with 2 keys “Width” and “Height”.<br>
RefreshLUTList()                                --&gt; Bool               # Refreshes LUT List</p>
<p class="has-line-data" data-line-start="179" data-line-end="188">MediaStorage<br>
GetMountedVolumeList()                          --&gt; [paths…]         # Returns list of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.<br>
GetSubFolderList(folderPath)                    --&gt; [paths…]         # Returns list of folder paths in the given absolute folder path.<br>
GetFileList(folderPath)                         --&gt; [paths…]         # Returns list of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.<br>
RevealInStorage(path)                           --&gt; None               # Expands and displays given file/folder path in Resolve’s Media Storage.<br>
AddItemListToMediaPool(item1, item2, …)       --&gt; [clips…]         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is one or more file/folder paths. Returns a list of the MediaPoolItems created.<br>
AddItemListToMediaPool([items…])              --&gt; [clips…]         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.<br>
AddClipMattesToMediaPool(MediaPoolItem, [paths], stereoEye) --&gt; Bool   # Adds specified media files as mattes for the specified MediaPoolItem. StereoEye is an optional argument for specifying which eye to add the matte to for stereo clips (“left” or “right”). Returns True if successful.<br>
AddTimelineMattesToMediaPool([paths])           --&gt; [MediaPoolItems]   # Adds specified media files as timeline mattes in current media pool folder. Returns a list of created MediaPoolItems.</p>
<p class="has-line-data" data-line-start="189" data-line-end="218">MediaPool<br>
GetRootFolder()                                 --&gt; Folder             # Returns root Folder of Media Pool<br>
AddSubFolder(folder, name)                      --&gt; Folder             # Adds new subfolder under specified Folder object with the given name.<br>
CreateEmptyTimeline(name)                       --&gt; Timeline           # Adds new timeline with given name.<br>
AppendToTimeline(clip1, clip2, …)             --&gt; Bool               # Appends specified MediaPoolItem objects in the current timeline. Returns True if successful.<br>
AppendToTimeline([clips])                       --&gt; Bool               # Appends specified MediaPoolItem objects in the current timeline. Returns True if successful.<br>
AppendToTimeline([{clipInfo}, …])             --&gt; Bool               # Appends list of clipInfos specified as dict of “mediaPoolItem”, “startFrame” (int), “endFrame” (int).<br>
CreateTimelineFromClips(name, clip1, clip2,…) --&gt; Timeline           # Creates new timeline with specified name, and appends the specified MediaPoolItem objects.<br>
CreateTimelineFromClips(name, [clips])          --&gt; Timeline           # Creates new timeline with specified name, and appends the specified MediaPoolItem objects.<br>
CreateTimelineFromClips(name, [{clipInfo}])     --&gt; Timeline           # Creates new timeline with specified name, appending the list of clipInfos specified as a dict of “mediaPoolItem”, “startFrame” (int), “endFrame” (int).<br>
ImportTimelineFromFile(filePath, {importOptions}) --&gt; Timeline         # Creates timeline based on parameters within given file and optional importOptions dict, with support for the keys:<br>
# “timelineName”: string, specifies the name of the timeline to be created<br>
# “importSourceClips”: Bool, specifies whether source clips should be imported, True by default<br>
# “sourceClipsPath”: string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if “importSourceClips” is True<br>
# “sourceClipsFolders”: List of Media Pool folder objects to search for source clips if the media is not present in current folder and if “importSourceClips” is False<br>
GetCurrentFolder()                              --&gt; Folder             # Returns currently selected Folder.<br>
SetCurrentFolder(Folder)                        --&gt; Bool               # Sets current folder by given Folder.<br>
DeleteClips([clips])                            --&gt; Bool               # Deletes specified clips or timeline mattes in the media pool<br>
DeleteFolders([subfolders])                     --&gt; Bool               # Deletes specified subfolders in the media pool<br>
MoveClips([clips], targetFolder)                --&gt; Bool               # Moves specified clips to target folder.<br>
MoveFolders([folders], targetFolder)            --&gt; Bool               # Moves specified folders to target folder.<br>
GetClipMatteList(MediaPoolItem)                 --&gt; [paths]            # Get mattes for specified MediaPoolItem, as a list of paths to the matte files.<br>
GetTimelineMatteList(Folder)                    --&gt; [MediaPoolItems]   # Get mattes in specified Folder, as list of MediaPoolItems.<br>
DeleteClipMattes(MediaPoolItem, [paths])        --&gt; Bool               # Delete mattes based on their file paths, for specified MediaPoolItem. Returns True on success.<br>
RelinkClips([MediaPoolItem], folderPath)        --&gt; Bool               # Update the folder location of specified media pool clips with the specified folder path.<br>
UnlinkClips([MediaPoolItem])                    --&gt; Bool               # Unlink specified media pool clips.<br>
ImportMedia([items…])                         --&gt; [MediaPoolItems]   # Imports specified file/folder paths into current Media Pool folder. Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.<br>
ExportMetadata(fileName, [clips])               --&gt; Bool               # Exports metadata of specified clips to ‘fileName’ in CSV format.<br>
# If no clips are specified, all clips from media pool will be used.</p>
<p class="has-line-data" data-line-start="219" data-line-end="223">Folder<br>
GetClipList()                                   --&gt; [clips…]         # Returns a list of clips (items) within the folder.<br>
GetName()                                       --&gt; string             # Returns the media folder name.<br>
GetSubFolderList()                              --&gt; [folders…]       # Returns a list of subfolders in the folder.</p>
<p class="has-line-data" data-line-start="224" data-line-end="253">MediaPoolItem<br>
GetName()                                       --&gt; string             # Returns the clip name.<br>
GetMetadata(metadataType=None)                  --&gt; string|dict        # Returns the metadata value for the key ‘metadataType’.<br>
# If no argument is specified, a dict of all set metadata properties is returned.<br>
SetMetadata(metadataType, metadataValue)        --&gt; Bool               # Sets the given metadata to metadataValue (string). Returns True if successful.<br>
GetMediaId()                                    --&gt; string             # Returns the unique ID for the MediaPoolItem.<br>
AddMarker(frameId, color, name, note, duration, --&gt; Bool               # Creates a new marker at given frameId position and with given marker information. ‘customData’ is optional and helps to attach user specific data to the marker.<br>
customData)<br>
GetMarkers()                                    --&gt; {markers…}       # Returns a dict (frameId -&gt; {information}) of all markers and dicts with their information.<br>
# Example of output format: {96.0: {‘color’: ‘Green’, ‘duration’: 1.0, ‘note’: ‘’, ‘name’: ‘Marker 1’, ‘customData’: ‘’}, …}<br>
# In the above example - there is one ‘Green’ marker at offset 96 (position of the marker)<br>
GetMarkerByCustomData(customData)               --&gt; {markers…}       # Returns marker {information} for the first matching marker with specified customData.<br>
UpdateMarkerCustomData(frameId, customData)     --&gt; Bool               # Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.<br>
GetMarkerCustomData(frameId)                    --&gt; string             # Returns customData string for the marker at given frameId position.<br>
DeleteMarkersByColor(color)                     --&gt; Bool               # Delete all markers of the specified color from the media pool item. “All” as argument deletes all color markers.<br>
DeleteMarkerAtFrame(frameNum)                   --&gt; Bool               # Delete marker at frame number from the media pool item.<br>
DeleteMarkerByCustomData(customData)            --&gt; Bool               # Delete first matching marker with specified customData.<br>
AddFlag(color)                                  --&gt; Bool               # Adds a flag with given color (string).<br>
GetFlagList()                                   --&gt; [colors…]        # Returns a list of flag colors assigned to the item.<br>
ClearFlags(color)                               --&gt; Bool               # Clears the flag of the given color if one exists. An “All” argument is supported and clears all flags.<br>
GetClipColor()                                  --&gt; string             # Returns the item color as a string.<br>
SetClipColor(colorName)                         --&gt; Bool               # Sets the item color based on the colorName (string).<br>
ClearClipColor()                                --&gt; Bool               # Clears the item color.<br>
GetClipProperty(propertyName=None)              --&gt; string|dict        # Returns the property value for the key ‘propertyName’.<br>
# If no argument is specified, a dict of all clip properties is returned. Check the section below for more information.<br>
SetClipProperty(propertyName, propertyValue)    --&gt; Bool               # Sets the given property to propertyValue (string). Check the section below for more information.<br>
LinkProxyMedia(propertyName)                    --&gt; Bool               # Links proxy media (absolute path) with the current clip.<br>
UnlinkProxyMedia()                              --&gt; Bool               # Unlinks any proxy media associated with clip.<br>
ReplaceClip(filePath)                           --&gt; Bool               # Replaces the underlying asset and metadata of MediaPoolItem with the specified absolute clip path.</p>
<p class="has-line-data" data-line-start="254" data-line-end="311">Timeline<br>
GetName()                                       --&gt; string             # Returns the timeline name.<br>
SetName(timelineName)                           --&gt; Bool               # Sets the timeline name if timelineName (string) is unique. Returns True if successful.<br>
GetStartFrame()                                 --&gt; int                # Returns the frame number at the start of timeline.<br>
GetEndFrame()                                   --&gt; int                # Returns the frame number at the end of timeline.<br>
GetTrackCount(trackType)                        --&gt; int                # Returns the number of tracks for the given track type (“audio”, “video” or “subtitle”).<br>
GetItemListInTrack(trackType, index)            --&gt; [items…]         # Returns a list of timeline items on that track (based on trackType and index). 1 &lt;= index &lt;= GetTrackCount(trackType).<br>
AddMarker(frameId, color, name, note, duration, --&gt; Bool               # Creates a new marker at given frameId position and with given marker information. ‘customData’ is optional and helps to attach user specific data to the marker.<br>
customData)<br>
GetMarkers()                                    --&gt; {markers…}       # Returns a dict (frameId -&gt; {information}) of all markers and dicts with their information.<br>
# Example: a value of {96.0: {‘color’: ‘Green’, ‘duration’: 1.0, ‘note’: ‘’, ‘name’: ‘Marker 1’, ‘customData’: ‘’}, …} indicates a single green marker at timeline offset 96<br>
GetMarkerByCustomData(customData)               --&gt; {markers…}       # Returns marker {information} for the first matching marker with specified customData.<br>
UpdateMarkerCustomData(frameId, customData)     --&gt; Bool               # Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.<br>
GetMarkerCustomData(frameId)                    --&gt; string             # Returns customData string for the marker at given frameId position.<br>
DeleteMarkersByColor(color)                     --&gt; Bool               # Deletes all timeline markers of the specified color. An “All” argument is supported and deletes all timeline markers.<br>
DeleteMarkerAtFrame(frameNum)                   --&gt; Bool               # Deletes the timeline marker at the given frame number.<br>
DeleteMarkerByCustomData(customData)            --&gt; Bool               # Delete first matching marker with specified customData.<br>
ApplyGradeFromDRX(path, gradeMode, item1, item2, …)–&gt; Bool          # Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - “No keyframes”, 1 - “Source Timecode aligned”, 2 - “Start Frames aligned”.<br>
ApplyGradeFromDRX(path, gradeMode, [items])     --&gt; Bool               # Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - “No keyframes”, 1 - “Source Timecode aligned”, 2 - “Start Frames aligned”.<br>
GetCurrentTimecode()                            --&gt; string             # Returns a string timecode representation for the current playhead position, while on Cut, Edit, Color and Deliver pages.<br>
GetCurrentVideoItem()                           --&gt; item               # Returns the current video timeline item.<br>
GetCurrentClipThumbnailImage()                  --&gt; {thumbnailData}    # Returns a dict (keys “width”, “height”, “format” and “data”) with data containing raw thumbnail image data (RGB 8-bit image data encoded in base64 format) for current media in the Color Page.<br>
# An example of how to retrieve and interpret thumbnails is provided in 6_get_current_media_thumbnail.py in the Examples folder.<br>
GetTrackName(trackType, trackIndex)             --&gt; string             # Returns the track name for track indicated by trackType (“audio”, “video” or “subtitle”) and index. 1 &lt;= trackIndex &lt;= GetTrackCount(trackType).<br>
SetTrackName(trackType, trackIndex, name)       --&gt; Bool               # Sets the track name (string) for track indicated by trackType (“audio”, “video” or “subtitle”) and index. 1 &lt;= trackIndex &lt;= GetTrackCount(trackType).<br>
DuplicateTimeline(timelineName)                 --&gt; timeline           # Duplicates the timeline and returns the created timeline, with the (optional) timelineName, on success.<br>
CreateCompoundClip([timelineItems], {clipInfo}) --&gt; timelineItem       # Creates a compound clip of input timeline items with an optional clipInfo map: {“startTimecode” : “00:00:00:00”, “name” : “Compound Clip 1”}. It returns the created timeline item.<br>
CreateFusionClip([timelineItems])               --&gt; timelineItem       # Creates a Fusion clip of input timeline items. It returns the created timeline item.<br>
Export(fileName, exportType, exportSubtype)     --&gt; Bool               # Exports timeline to ‘fileName’ as per input exportType &amp; exportSubtype format.<br>
# exportType can be one of the following constants:<br>
#   resolve.EXPORT_AAF<br>
#   resolve.EXPORT_DRT<br>
#   resolve.EXPORT_EDL<br>
#   resolve.EXPORT_FCP_7_XML<br>
#   resolve.EXPORT_FCPXML_1_3<br>
#   resolve.EXPORT_FCPXML_1_4<br>
#   resolve.EXPORT_FCPXML_1_5<br>
#   resolve.EXPORT_FCPXML_1_6<br>
#   resolve.EXPORT_FCPXML_1_7<br>
#   resolve.EXPORT_FCPXML_1_8<br>
#   resolve.EXPORT_HDR_10_PROFILE_A<br>
#   resolve.EXPORT_HDR_10_PROFILE_B<br>
#   resolve.EXPORT_TEXT_CSV<br>
#   resolve.EXPORT_TEXT_TAB<br>
#   resolve.EXPORT_DOLBY_VISION_VER_2_9<br>
#   resolve.EXPORT_DOLBY_VISION_VER_4_0<br>
# exportSubtype can be one of the following enums:<br>
#   resolve.EXPORT_NONE<br>
#   resolve.EXPORT_AAF_NEW<br>
#   resolve.EXPORT_AAF_EXISTING<br>
#   resolve.EXPORT_CDL<br>
#   resolve.EXPORT_SDL<br>
#   resolve.EXPORT_MISSING_CLIPS<br>
# Please note that exportSubType is a required parameter for resolve.EXPORT_AAF and resolve.EXPORT_EDL. For rest of the exportType, exportSubtype is ignored.<br>
# When exportType is resolve.EXPORT_AAF, valid exportSubtype values are resolve.EXPORT_AAF_NEW and resolve.EXPORT_AAF_EXISTING.<br>
# When exportType is resolve.EXPORT_EDL, valid exportSubtype values are resolve.EXPORT_CDL, resolve.EXPORT_SDL, resolve.EXPORT_MISSING_CLIPS and resolve.EXPORT_NONE.<br>
# Note: Replace ‘resolve.’ when using the constants above, if a different Resolve class instance name is used.</p>
<p class="has-line-data" data-line-start="312" data-line-end="367">TimelineItem<br>
GetName()                                       --&gt; string             # Returns the item name.<br>
GetDuration()                                   --&gt; int                # Returns the item duration.<br>
GetEnd()                                        --&gt; int                # Returns the end frame position on the timeline.<br>
GetFusionCompCount()                            --&gt; int                # Returns number of Fusion compositions associated with the timeline item.<br>
GetFusionCompByIndex(compIndex)                 --&gt; fusionComp         # Returns the Fusion composition object based on given index. 1 &lt;= compIndex &lt;= timelineItem.GetFusionCompCount()<br>
GetFusionCompNameList()                         --&gt; [names…]         # Returns a list of Fusion composition names associated with the timeline item.<br>
GetFusionCompByName(compName)                   --&gt; fusionComp         # Returns the Fusion composition object based on given name.<br>
GetLeftOffset()                                 --&gt; int                # Returns the maximum extension by frame for clip from left side.<br>
GetRightOffset()                                --&gt; int                # Returns the maximum extension by frame for clip from right side.<br>
GetStart()                                      --&gt; int                # Returns the start frame position on the timeline.<br>
AddMarker(frameId, color, name, note, duration, --&gt; Bool               # Creates a new marker at given frameId position and with given marker information. ‘customData’ is optional and helps to attach user specific data to the marker.<br>
customData)<br>
GetMarkers()                                    --&gt; {markers…}       # Returns a dict (frameId -&gt; {information}) of all markers and dicts with their information.<br>
# Example: a value of {96.0: {‘color’: ‘Green’, ‘duration’: 1.0, ‘note’: ‘’, ‘name’: ‘Marker 1’, ‘customData’: ‘’}, …} indicates a single green marker at clip offset 96<br>
GetMarkerByCustomData(customData)               --&gt; {markers…}       # Returns marker {information} for the first matching marker with specified customData.<br>
UpdateMarkerCustomData(frameId, customData)     --&gt; Bool               # Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.<br>
GetMarkerCustomData(frameId)                    --&gt; string             # Returns customData string for the marker at given frameId position.<br>
DeleteMarkersByColor(color)                     --&gt; Bool               # Delete all markers of the specified color from the timeline item. “All” as argument deletes all color markers.<br>
DeleteMarkerAtFrame(frameNum)                   --&gt; Bool               # Delete marker at frame number from the timeline item.<br>
DeleteMarkerByCustomData(customData)            --&gt; Bool               # Delete first matching marker with specified customData.<br>
AddFlag(color)                                  --&gt; Bool               # Adds a flag with given color (string).<br>
GetFlagList()                                   --&gt; [colors…]        # Returns a list of flag colors assigned to the item.<br>
ClearFlags(color)                               --&gt; Bool               # Clear flags of the specified color. An “All” argument is supported to clear all flags.<br>
GetClipColor()                                  --&gt; string             # Returns the item color as a string.<br>
SetClipColor(colorName)                         --&gt; Bool               # Sets the item color based on the colorName (string).<br>
ClearClipColor()                                --&gt; Bool               # Clears the item color.<br>
AddFusionComp()                                 --&gt; fusionComp         # Adds a new Fusion composition associated with the timeline item.<br>
ImportFusionComp(path)                          --&gt; fusionComp         # Imports a Fusion composition from given file path by creating and adding a new composition for the item.<br>
ExportFusionComp(path, compIndex)               --&gt; Bool               # Exports the Fusion composition based on given index to the path provided.<br>
DeleteFusionCompByName(compName)                --&gt; Bool               # Deletes the named Fusion composition.<br>
LoadFusionCompByName(compName)                  --&gt; fusionComp         # Loads the named Fusion composition as the active composition.<br>
RenameFusionCompByName(oldName, newName)        --&gt; Bool               # Renames the Fusion composition identified by oldName.<br>
AddVersion(versionName, versionType)            --&gt; Bool               # Adds a new color version for a video clipbased on versionType (0 - local, 1 - remote).<br>
DeleteVersionByName(versionName, versionType)   --&gt; Bool               # Deletes a color version by name and versionType (0 - local, 1 - remote).<br>
LoadVersionByName(versionName, versionType)     --&gt; Bool               # Loads a named color version as the active version. versionType: 0 - local, 1 - remote.<br>
RenameVersionByName(oldName, newName, versionType)–&gt; Bool             # Renames the color version identified by oldName and versionType (0 - local, 1 - remote).<br>
GetVersionNameList(versionType)                 --&gt; [names…]         # Returns a list of all color versions for the given versionType (0 - local, 1 - remote).<br>
GetMediaPoolItem()                              --&gt; MediaPoolItem      # Returns the media pool item corresponding to the timeline item if one exists.<br>
GetStereoConvergenceValues()                    --&gt; {keyframes…}     # Returns a dict (offset -&gt; value) of keyframe offsets and respective convergence values.<br>
GetStereoLeftFloatingWindowParams()             --&gt; {keyframes…}     # For the LEFT eye -&gt; returns a dict (offset -&gt; dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.<br>
GetStereoRightFloatingWindowParams()            --&gt; {keyframes…}     # For the RIGHT eye -&gt; returns a dict (offset -&gt; dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.<br>
SetLUT(nodeIndex, lutPath)                      --&gt; Bool               # Sets LUT on the node mapping the node index provided, 1 &lt;= nodeIndex &lt;= total number of nodes.<br>
# The lutPath can be an absolute path, or a relative path (based off custom LUT paths or the master LUT path).<br>
# The operation is successful for valid lut paths that Resolve has already discovered (see Project.RefreshLUTList).<br>
SetCDL([CDL map])                               --&gt; Bool               # Keys of map are: “NodeIndex”, “Slope”, “Offset”, “Power”, “Saturation”, where 1 &lt;= NodeIndex &lt;= total number of nodes.<br>
# Example python code - SetCDL({“NodeIndex” : “1”, “Slope” : “0.5 0.4 0.2”, “Offset” : “0.4 0.3 0.2”, “Power” : “0.6 0.7 0.8”, “Saturation” : “0.65”})<br>
AddTake(mediaPoolItem, startFrame=0, endFrame)=0    --&gt; Bool           # Adds mediaPoolItem as a new take. Initializes a take selector for the timeline item if needed. By default, the whole clip is added. startFrame and endFrame can be specified as extents.<br>
GetSelectedTakeIndex()                          --&gt; int                # Returns the index of the currently selected take, or 0 if the clip is not a take selector.<br>
GetTakesCount()                                 --&gt; int                # Returns the number of takes in take selector, or 0 if the clip is not a take selector.<br>
GetTakeByIndex(idx)                             --&gt; {takeInfo…}      # Returns a dict (keys “startFrame”, “endFrame” and “mediaPoolItem”) with take info for specified index.<br>
DeleteTakeByIndex(idx)                          --&gt; Bool               # Deletes a take by index, 1 &lt;= idx &lt;= number of takes.<br>
SelectTakeByIndex(idx)                          --&gt; Bool               # Selects a take by index, 1 &lt;= idx &lt;= number of takes.<br>
FinalizeTake()                                  --&gt; Bool               # Finalizes take selection.<br>
CopyGrades([tgtTimelineItems])                  --&gt; Bool               # Copies the current grade to all the items in tgtTimelineItems list. Returns True on success and False if any error occured.</p>
<h2 class="code-line" data-line-start=369 data-line-end=371 ><a id="List_and_Dict_Data_Structures_369"></a>List and Dict Data Structures</h2>
<p class="has-line-data" data-line-start="371" data-line-end="374">Beside primitive data types, Resolve’s Python API mainly uses list and dict data structures. Lists are denoted by [ … ] and dicts are denoted by { … } above.<br>
As Lua does not support list and dict data structures, the Lua API implements “list” as a table with indices, e.g. { [1] = listValue1, [2] = listValue2, … }.<br>
Similarly the Lua API implements “dict” as a table with the dictionary key as first element, e.g. { [dictKey1] = dictValue1, [dictKey2] = dictValue2, … }.</p>
<h2 class="code-line" data-line-start=376 data-line-end=378 ><a id="Looking_up_Project_and_Clip_properties_376"></a>Looking up Project and Clip properties</h2>
<p class="has-line-data" data-line-start="378" data-line-end="380">This section covers additional notes for the functions “Project:GetSetting”, “Project:SetSetting”, “MediaPoolItem:GetClipProperty” and “MediaPoolItem:SetClipProperty”. These functions are used to get<br>
and set properties otherwise available to the user through the Project Settings and the Clip Attributes dialogs.</p>
<p class="has-line-data" data-line-start="381" data-line-end="383">The functions follow a key-value pair format, where each property is identified by a key (the settingName or propertyName parameter) and possesses a value (typically a text value). Keys and values are<br>
designed to be easily correlated with parameter names and values in the Resolve UI. Explicitly enumerated values for some parameters are listed below.</p>
<p class="has-line-data" data-line-start="384" data-line-end="386">Some properties may be read only - these include intrinsic clip properties like date created or sample rate, and properties that can be disabled in specific application contexts (e.g. custom colorspaces<br>
in an ACES workflow, or output sizing parameters when behavior is set to match timeline)</p>
<p class="has-line-data" data-line-start="387" data-line-end="391">Getting values:<br>
Invoke “Project:GetSetting” or “MediaPoolItem:GetClipProperty” with the appropriate property key. To get a snapshot of all queryable properties (keys and values), you can call “Project:GetSetting” or<br>
“MediaPoolItem:GetClipProperty” without parameters (or with a NoneType or a blank property key). Using specific keys to query individual properties will be faster. Note that getting a property using an<br>
invalid key will return a trivial result.</p>
<p class="has-line-data" data-line-start="392" data-line-end="395">Setting values:<br>
Invoke “Project:SetSetting” or “MediaPoolItem:SetClipProperty” with the appropriate property key and a valid value. When setting a parameter, please check the return value to ensure the success of the<br>
operation. You can troubleshoot the validity of keys and values by setting the desired result from the UI and checking property snapshots before and after the change.</p>
<p class="has-line-data" data-line-start="396" data-line-end="400">The following Project properties have specifically enumerated values:<br>
“superScale” - the property value is an enumerated integer between 0 and 3 with these meanings: 0=Auto, 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.<br>
Affects:<br>
• x = Project:GetSetting(‘superScale’) and Project:SetSetting(‘superScale’, x)</p>
<p class="has-line-data" data-line-start="401" data-line-end="405">“timelineFrameRate” - the property value is one of the frame rates available to the user in project settings under “Timeline frame rate” option. Drop Frame can be configured for supported frame rates<br>
by appending the frame rate with “DF”, e.g. “29.97 DF” will enable drop frame and “29.97” will disable drop frame<br>
Affects:<br>
• x = Project:GetSetting(‘timelineFrameRate’) and Project:SetSetting(‘timelineFrameRate’, x)</p>
<p class="has-line-data" data-line-start="406" data-line-end="410">The following Clip properties have specifically enumerated values:<br>
“superScale” - the property value is an enumerated integer between 1 and 3 with these meanings: 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.<br>
Affects:<br>
• x = MediaPoolItem:GetClipProperty(‘Super Scale’) and MediaPoolItem:SetClipProperty(‘Super Scale’, x)</p>
<h2 class="code-line" data-line-start=412 data-line-end=414 ><a id="Deprecated_Resolve_API_Functions_412"></a>Deprecated Resolve API Functions</h2>
<p class="has-line-data" data-line-start="414" data-line-end="415">The following API functions are deprecated.</p>
<p class="has-line-data" data-line-start="416" data-line-end="419">ProjectManager<br>
GetProjectsInCurrentFolder()                    --&gt; {project names…} # Returns a dict of project names in current folder.<br>
GetFoldersInCurrentFolder()                     --&gt; {folder names…}  # Returns a dict of folder names in current folder.</p>
<p class="has-line-data" data-line-start="420" data-line-end="424">Project<br>
GetPresets()                                    --&gt; {presets…}       # Returns a dict of presets and their information.<br>
GetRenderJobs()                                 --&gt; {render jobs…}   # Returns a dict of render jobs and their information.<br>
GetRenderPresets()                              --&gt; {presets…}       # Returns a dict of render presets and their information.</p>
<p class="has-line-data" data-line-start="425" data-line-end="431">MediaStorage<br>
GetMountedVolumes()                             --&gt; {paths…}         # Returns a dict of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.<br>
GetSubFolders(folderPath)                       --&gt; {paths…}         # Returns a dict of folder paths in the given absolute folder path.<br>
GetFiles(folderPath)                            --&gt; {paths…}         # Returns a dict of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.<br>
AddItemsToMediaPool(item1, item2, …)          --&gt; {clips…}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is one or more file/folder paths. Returns a dict of the MediaPoolItems created.<br>
AddItemsToMediaPool([items…])                 --&gt; {clips…}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. Returns a dict of the MediaPoolItems created.</p>
<p class="has-line-data" data-line-start="432" data-line-end="435">Folder<br>
GetClips()                                      --&gt; {clips…}         # Returns a dict of clips (items) within the folder.<br>
GetSubFolders()                                 --&gt; {folders…}       # Returns a dict of subfolders in the folder.</p>
<p class="has-line-data" data-line-start="436" data-line-end="438">MediaPoolItem<br>
GetFlags()                                      --&gt; {colors…}        # Returns a dict of flag colors assigned to the item.</p>
<p class="has-line-data" data-line-start="439" data-line-end="441">Timeline<br>
GetItemsInTrack(trackType, index)               --&gt; {items…}         # Returns a dict of Timeline items on the video or audio track (based on trackType) at specified</p>
<p class="has-line-data" data-line-start="442" data-line-end="446">TimelineItem<br>
GetFusionCompNames()                            --&gt; {names…}         # Returns a dict of Fusion composition names associated with the timeline item.<br>
GetFlags()                                      --&gt; {colors…}        # Returns a dict of flag colors assigned to the item.<br>
GetVersionNames(versionType)                    --&gt; {names…}         # Returns a dict of version names by provided versionType: 0 - local, 1 - remote.</p>
<h2 class="code-line" data-line-start=448 data-line-end=450 ><a id="Unsupported_Resolve_API_Functions_448"></a>Unsupported Resolve API Functions</h2>
<p class="has-line-data" data-line-start="450" data-line-end="451">The following API (functions and paraameters) are no longer supported.</p>
<p class="has-line-data" data-line-start="452" data-line-end="459">Project<br>
StartRendering(index1, index2, …)             --&gt; Bool               # Please use unique job ids (string) instead of indices.<br>
StartRendering([idxs…])                       --&gt; Bool               # Please use unique job ids (string) instead of indices.<br>
DeleteRenderJobByIndex(idx)                     --&gt; Bool               # Please use unique job ids (string) instead of indices.<br>
GetRenderJobStatus(idx)                         --&gt; {status info}      # Please use unique job ids (string) instead of indices.<br>
GetSetting and SetSetting                       --&gt; {}                 # settingName “videoMonitorUseRec601For422SDI” is no longer supported.<br>
# Please use “videoMonitorUseMatrixOverrideFor422SDI” and “videoMonitorMatrixOverrideFor422SDI” instead.</p>