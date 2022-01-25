# GUI Automator for (Re)Programming Devices

### PyAutoGUI for Partial Automation

This tool was designed to take the annoying tedium out of a repetitive task, and then double output by a given worker.

On occasions when devices already in our possession (usually at our warehouse) needed reprogramming, we had to:

1. Connect a device via USB serial cable.
1. Open a proprietary tool, enter a password, and connect to the device over serial.
2. Load a configuration file, and verify it was loaded, even if one line needed to be changed.
3. Click a button and verify output was correct visually.
4. Close that tool and open another, enter a password, and connect to the device over serial.
5. Load a weird screen not found in any menu, enter a line of text, and hit send.
6. Click a button and verify output was correct visually, again.
7. Disconnect device and rebox.

This really took a lot of unnecessary time and attention, and was error-prone.

After using this tool, there was a one-time setup process per PC:

1. Create shortcuts for the proprietary tools.
2. Set specific keyboard shortcuts for the tools.
3. Download the PyInstaller exe of this tool.
4. Run the .exe

Now, the process looks more like this:

1. Connect a device via USB serial cable.
2. Hit any non-quitting key.
3. Wait and visually inspect when you hear the tool "ding."
4. Wait and visually inspect when you hear the tool "ding" again.
5. Disconnect device and rebox.

This process is no longer error-prone due to user input, and the physical task of unboxing and reboxing can be done while the tool does its thing. Experienced workers can actually manage two separate computers and do two devices at a time relatively easily, while a second worker focuses on reboxing. It also makes it easier for a worker to prepare a bunch of devices, go through them one at a time, and rebox them all while on a conference call or participating in an in-person discussion.

As the proprietary tools changed, this was updated as well relatively easily.

### Deployment with Py2Exe

Initially, I had deployed this tool with Py2Exe. PyInstaller seemed more robust, but Py2Exe did the job just fine and none of the extra bells and whistles of PyInstaller seemed to benefit the project.