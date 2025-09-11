"""Take screenshot of stimulus"""

# The category determines the group for the plugin in the item toolbar
category = "Screenshot"
# Defines the GUI controls
controls = [
    {
        "type": "checkbox",
        "var": "verbose",
        "label": "Verbose mode",
        "name": "checkbox_verbose_mode",
        "tooltip": "Run in verbose mode"
    },  {
        "type": "checkbox",
        "var": "window_stim_psycho",
        "label": "Stimulus display (PsychoPy)",
        "name": "checkbox_window_stim_psycho",
        "tooltip": "Stimulus display (PsychoPy)"
    },  {
        "type": "checkbox",
        "var": "window_stim_pil",
        "label": "Stimulus display (PIL)",
        "name": "checkbox_window_stim_pil",
        "tooltip": "Stimulus display (PIL)"
    },  {
        "type": "checkbox",
        "var": "window_full_pil",
        "label": "Composite of all displays (PIL)",
        "name": "checkbox_window_full_pil",
        "tooltip": "Composite of all displays (PIL)"
    },  {
        "type": "line_edit",
        "var": "filename_screenshot",
        "label": "Filename",
        "name": "line_edit_filename_screenshot",
        "info": "Filename with extension, extension determines the picture format (.png; .jpg; etc.)",
        "tooltip": "Filename"
    }, {
        "type": "text",
        "label": "<small>Screenshot version 0.6.0</small>"
    }
]
