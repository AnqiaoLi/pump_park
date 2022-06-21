# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj")

# Code for /obj/geo1
hou_node = hou_parent.createNode("geo", "geo1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-3.71821, 1.80769))
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hideLabel(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template2.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_1", "Render", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template2.setTags({"spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0", "Shading", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("A list of tags which can be used to select the object")
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be reflected on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be refracted on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Lights that illuminate this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_1", "Sampling", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template3.setTags({"spare_category": "Sampling"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_2", "Dicing", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_3", "Geometry", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_2", "Misc", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Any, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"filechooser_mode": "read"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pre_xform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pre_xform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("clean")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/keeppos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("keeppos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/childcomp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("childcomp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/constraints_on parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("constraints_on")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/constraints_path parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("constraints_path")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookatpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookatpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookupobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookupobjpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("on")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pathobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pathobjpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/roll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("roll")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uparmtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("uparmtype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pathorient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pathorient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/up parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("up")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bank parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("bank")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_materialpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_materialpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_materialopts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_materialopts")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("override")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/tdisplay parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("tdisplay")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/display parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("display")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/use_dcolor parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("use_dcolor")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/dcolor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("dcolor")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/picking parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("picking")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pickscript parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pickscript")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/caching parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("caching")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_shadeopen parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_shadeopen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_displayassubdiv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_displayassubdiv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_onionskin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_onionskin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/stdswitcher41 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("stdswitcher41")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendervisibility parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendervisibility")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendersubd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendersubd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_subdstyle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_subdstyle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mantra_catclark")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_subdgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_subdgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_quality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_quality")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_vtxinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_vtxinterp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_fvarinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_fvarinterp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/categories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("categories")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/reflectmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("reflectmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/refractmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("refractmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lightmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lightmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lightcategories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lightcategories")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_lpetag parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_lpetag")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_volumefilter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_volumefilter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("box")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_volumefilterwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_volumefilterwidth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_matte parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_matte")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rayshade parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rayshade")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/geo_velocityblur parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("geo_velocityblur")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/geo_accelattribute parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("geo_accelattribute")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("accel")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_shadingquality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_shadingquality")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_flatness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_flatness")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.050000000000000003)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_raypredice parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_raypredice")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_curvesurface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_curvesurface")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rmbackface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rmbackface")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_geometrypath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_geometrypath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_forcegeometry parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_forcegeometry")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendersubdcurves parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendersubdcurves")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_renderpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_renderpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_renderpointsas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_renderpointsas")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_usenforpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_usenforpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_pointscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_pointscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_pscalediameter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_pscalediameter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_metavolume parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_metavolume")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_coving parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_coving")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_materialoverride parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_materialoverride")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("compact")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_overridedetail parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_overridedetail")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_procuseroottransform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_procuseroottransform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

# Code to establish connections for /obj/geo1
hou_node = hou_parent.node("geo1")
if hou_parent.node("geo2") is not None:
    hou_node.setInput(0, hou_parent.node("geo2"), 0)
hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/resample1
hou_node = hou_parent.createNode("resample", "resample1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.375432, -1.41856))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/resample1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/maintainprimorder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("maintainprimorder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/lod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("lod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/edge parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("edge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("dist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/measure parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("measure")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/dolength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("dolength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/length parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("length")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.16)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/dosegs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("dosegs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/segs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("segs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/useattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("useattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/allequal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("allequal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/last parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("last")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/randomshift parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("randomshift")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/onlypoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("onlypoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/treatpolysas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("treatpolysas")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("subd")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/outputsubdpoly parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("outputsubdpoly")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/doptdistattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("doptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/ptdistattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("ptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ptdist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/dotangentattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("dotangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/tangentattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("tangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("N")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/docurveuattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("docurveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/curveuattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("curveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curveu")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/docurvenumattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("docurvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample1/curvenumattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample1")
hou_parm = hou_node.parm("curvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curvenum")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/curv_dirs
hou_node = hou_parent.createNode("attribwrangle", "curv_dirs", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.0563972, -2.81323))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/curv_dirs/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("vector flatnrm = @N;\nflatnrm.y = 0;\nflatnrm = normalize(flatnrm);\n\nv@right = cross({0, 1, 0}, flatnrm);\nv@up = cross(@N, @right);\n\nv@oldnorm = @N;\n@N = v@right;")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/curv_dirs/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/curv_dirs")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/bank_ratio
hou_node = hou_parent.createNode("subnet", "bank_ratio", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.53746, -3.99254))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/label1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio")
hou_parm = hou_node.parm("label1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #1")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/label2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio")
hou_parm = hou_node.parm("label2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #2")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/label3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio")
hou_parm = hou_node.parm("label3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #3")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/label4 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio")
hou_parm = hou_node.parm("label4")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #4")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/bank_ratio/convertline1
hou_node = hou_parent.createNode("convertline", "convertline1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.81909, 4.13336))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/convertline1/computelength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/convertline1")
hou_parm = hou_node.parm("computelength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/convertline1/lengthname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/convertline1")
hou_parm = hou_node.parm("lengthname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("restlength")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/bank_ratio/peak1
hou_node = hou_parent.createNode("peak", "peak1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0, 5.2176))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/peak1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/peak1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/peak1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/peak1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/peak1/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/peak1")
hou_parm = hou_node.parm("dist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.80000000000000004)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/peak1/updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/peak1")
hou_parm = hou_node.parm("updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/bank_ratio/convertline2
hou_node = hou_parent.createNode("convertline", "convertline2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0, 4.13336))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/convertline2/computelength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/convertline2")
hou_parm = hou_node.parm("computelength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/convertline2/lengthname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/convertline2")
hou_parm = hou_node.parm("lengthname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("restlength")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/bank_ratio/bank_ratio
hou_node = hou_parent.createNode("attribwrangle", "bank_ratio", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.86287, 2.74097))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/bank_ratio/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("float otherlength = prim(1, \"restlength\", @primnum);\nf@bank_ratio = f@restlength/otherlength;\n")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/bank_ratio/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/bank_ratio")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/bank_ratio/attribpromote1
hou_node = hou_parent.createNode("attribpromote", "attribpromote1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.95988, 1.54499))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bank_ratio/attribpromote1/inname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("inname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bank_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/inclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("inclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/outclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("outclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/usepieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("usepieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/pieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("pieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("name")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mean")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/useoutname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("useoutname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/outname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("outname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bank_ratio/attribpromote1/deletein parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bank_ratio/attribpromote1")
hou_parm = hou_node.parm("deletein")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/geo1/bank_ratio/convertline1
hou_node = hou_parent.node("convertline1")
if len(hou_parent.indirectInputs()) > 0:
    hou_node.setInput(0, hou_parent.indirectInputs()[0])
# Code to establish connections for /obj/geo1/bank_ratio/peak1
hou_node = hou_parent.node("peak1")
if len(hou_parent.indirectInputs()) > 0:
    hou_node.setInput(0, hou_parent.indirectInputs()[0])
# Code to establish connections for /obj/geo1/bank_ratio/convertline2
hou_node = hou_parent.node("convertline2")
if hou_parent.node("peak1") is not None:
    hou_node.setInput(0, hou_parent.node("peak1"), 0)
# Code to establish connections for /obj/geo1/bank_ratio/bank_ratio
hou_node = hou_parent.node("bank_ratio")
if hou_parent.node("convertline1") is not None:
    hou_node.setInput(0, hou_parent.node("convertline1"), 0)
if hou_parent.node("convertline2") is not None:
    hou_node.setInput(1, hou_parent.node("convertline2"), 0)
# Code to establish connections for /obj/geo1/bank_ratio/attribpromote1
hou_node = hou_parent.node("attribpromote1")
if hou_parent.node("bank_ratio") is not None:
    hou_node.setInput(0, hou_parent.node("bank_ratio"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/attribtransfer1
hou_node = hou_parent.createNode("attribtransfer", "attribtransfer1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.160441, -4.98579))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/attribtransfer1/srcgroups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("srcgroups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/srcgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("srcgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/dstgroups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("dstgroups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/dstgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("dstgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/cardswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("cardswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/detailattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("detailattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/detailattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("detailattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/primitiveattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("primitiveattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/primattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("primattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/pointattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("pointattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/pointattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("pointattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/vertexattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("vertexattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/vertexattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("vertexattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/copyvariable parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("copyvariable")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/matchpattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("matchpattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/kernel parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("kernel")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("elendt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/kernelradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("kernelradius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/maxsamplecount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("maxsamplecount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/threshold parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("threshold")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/thresholddist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("thresholddist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/blendwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("blendwidth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribtransfer1/uniformbias parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribtransfer1")
hou_parm = hou_node.parm("uniformbias")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/visualize1
hou_node = hou_parent.createNode("visualize", "visualize1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(5.45959, -10.4294))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setvisualizers", "Update Visualizers", default_value=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("clearvisualizers", "Clear Incoming Visualizers", default_value=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setvisualizers == 0 }")
hou_parm_template.setTags({"autoscope": "0000000000000000"})
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("wireframe", "Wireframe", menu_items=(["nochange","shaded","viewport","wireframe"]), menu_labels=(["No Change","Force Shaded","Use Viewport Settings","Force Wireframe"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("lit", "Lighting", menu_items=(["nochange","unlit","lit"]), menu_labels=(["No Change","Unlit","Lit"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("xray", "X-Ray", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setcuspangle", "Set Cusp Angle", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("cuspangle", "Cusp Angle", 1, default_value=([60]), min=0, max=180, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setcuspangle == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("showpoints", "Show Points", menu_items=(["nochange","unconnected","all"]), menu_labels=(["No Change","Unconnected","All"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spherepoints", "Points as Spheres", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spriteblend", "Sprite Blending", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setspritecutoff", "Set Sprite Cutoff", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("spritecutoff", "Sprite Cutoff", 1, default_value=([0.5]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setspritecutoff == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("node_vis_enabled", "Visualization Enabled", default_value=True)
hou_parm_template.hide(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("num_visualizers", "Visualizers", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template.hide(True)
hou_parm_template.setTags({"multistartoffset": "0"})
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vis_active#", "Active #", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vis_data#", "Raw Data #", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.hideLabel(True)
hou_parm_template2.setTags({"editor": "1"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/visualize1/setvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("setvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/clearvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("clearvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/wireframe parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("wireframe")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/lit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("lit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/xray parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("xray")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/setcuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("setcuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/cuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("cuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(60)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/showpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("showpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/spherepoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("spherepoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/spriteblend parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("spriteblend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/setspritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("setspritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/spritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("spritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/node_vis_enabled parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("node_vis_enabled")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/num_visualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("num_visualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/vis_active0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("vis_active0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/visualize1/vis_data0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/visualize1")
hou_parm = hou_node.parm("vis_data0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("{\n\t\"flags\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":27\n\t},\n\t\"icon\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"VIEW_visualization_color\"\n\t},\n\t\"label\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"Color 1\"\n\t},\n\t\"name\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_color_1\"\n\t},\n\t\"parameters\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"{\\nversion 0.8\\nstyle\\t[ 0\\tlocks=0 ]\\t(\\t\\\"text\\\"\\t)\\nclass\\t[ 0\\tlocks=0 ]\\t(\\t\\\"point\\\"\\t)\\nattrib\\t[ 0\\tlocks=0 ]\\t(\\tbank_ratio\\t)\\nvisibility\\t[ 0\\tlocks=0 ]\\t(\\t\\\"always\\\"\\t)\\ndecorradius\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ngroup\\t[ 0\\tlocks=0 ]\\t(\\t\\\"\\\"\\t)\\npointsize\\t[ 0\\tlocks=0 ]\\t(\\t3\\t)\\nlengthscale\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nunitlength\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nnormalize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\narrowheads\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\nvectorcoloring\\t[ 0\\tlocks=0 ]\\t(\\t\\\"fixed\\\"\\t)\\ncolorattrib\\t[ 0\\tlocks=0 ]\\t(\\tCd\\t)\\nramptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"false\\\"\\t)\\ncolorramp\\t[ 0\\tlocks=0 ]\\t(\\t5\\t)\\nrangespec\\t[ 0\\tlocks=0 ]\\t(\\t\\\"center-width\\\"\\t)\\nminscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nmaxscalar\\t[ 0\\tlocks=0 ]\\t(\\t10\\t)\\ncenterscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nwidthscalar\\t[ 0\\tlocks=0 ]\\t(\\t2\\t)\\nclamptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"edge\\\"\\t)\\ntreatasscalar\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\nusing\\t[ 0\\tlocks=0 ]\\t(\\t\\\"length\\\"\\t)\\ncomponent\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrefvec\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t)\\nmarkercolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t1\\t)\\ntrail\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t0.5\\t)\\ntextcolor\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t0.75\\t0.75\\t)\\nfontsize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"guidefont\\\"\\t)\\nxcolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\nycolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t1\\t)\\nzcolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t1\\t1\\t)\\ncolorramp1pos\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp1c\\t[ 0\\tlocks=0 ]\\t(\\t0.20000000298023224\\t0\\t1\\t)\\ncolorramp1interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp2pos\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t)\\ncolorramp2c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0.85000002384185791\\t1\\t)\\ncolorramp2interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp3pos\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ncolorramp3c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0.10000000149011612\\t)\\ncolorramp3interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp4pos\\t[ 0\\tlocks=0 ]\\t(\\t0.75\\t)\\ncolorramp4c\\t[ 0\\tlocks=0 ]\\t(\\t0.94999998807907104\\t1\\t0\\t)\\ncolorramp4interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp5pos\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncolorramp5c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ncolorramp5interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\n}\\n\"\n\t},\n\t\"scope\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":2\n\t},\n\t\"type\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_marker\"\n\t}\n}\n")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/min_ratio
hou_node = hou_parent.createNode("attribpromote", "min_ratio", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.02478, -6.24421))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/min_ratio/inname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("inname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bank_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/inclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("inclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/outclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("outclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("detail")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/usepieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("usepieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/pieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("pieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("name")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/useoutname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("useoutname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/outname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("outname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/min_ratio/deletein parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/min_ratio")
hou_parm = hou_node.parm("deletein")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/max_ratio
hou_node = hou_parent.createNode("attribpromote", "max_ratio", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.02478, -7.37119))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/max_ratio/inname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("inname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bank_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/inclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("inclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/outclass parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("outclass")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("detail")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/usepieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("usepieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/pieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("pieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("name")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("max")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/useoutname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("useoutname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/outname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("outname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("max_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/max_ratio/deletein parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/max_ratio")
hou_parm = hou_node.parm("deletein")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/attribremap1
hou_node = hou_parent.createNode("attribremap", "attribremap1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.02823, -8.57659))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/attribremap1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/inname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("inname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bank_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/outname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("outname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bank_ratio")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/computerange parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("computerange")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/inputmin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("inputmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.81078779697418213)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"min_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"min_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"min_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"min_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/attribremap1/inputmax parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("inputmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1.3085587024688721)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(1)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"max_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(1)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"max_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(1)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"max_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(1)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("detail(0, \"max_ratio\", 0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/attribremap1/outputmin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("outputmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(-1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/outputmax parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("outputmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/clamptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("clamptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("edge")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/useramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("useramp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap1pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap1value")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap1interp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("linear")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap2pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap2value")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/attribremap1/remap2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribremap1")
hou_parm = hou_node.parm("remap2interp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("linear")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/banking
hou_node = hou_parent.createNode("attribwrangle", "banking", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.02823, -9.52897))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1", "Code", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("group", "Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a attribvop1 bindgroup", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringToggle)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_action": "import soputils\nkwargs['geometrytype'] = kwargs['node'].parmTuple('grouptype')\nkwargs['inputindex'] = 0\nsoputils.selectGroupParm(kwargs)", "script_action_help": "Select geometry from an available viewport.", "script_action_icon": "BUTTONS_reselect"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("grouptype", "Group Type", menu_items=(["guess","vertices","edges","points","prims"]), menu_labels=(["Guess from Group","Vertices","Edges","Points","Primitives"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("class", "Run Over", menu_items=(["detail","primitive","point","vertex","number"]), menu_labels=(["Detail (only once)","Primitives","Points","Vertices","Numbers"]), default_value=2, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_numcount", "Number Count", 1, default_value=([10]), min=0, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_threadjobsize", "Thread Job Size", 1, default_value=([1024]), min=1, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("snippet", "VEXpression", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="import vexpressionmenu\n\nreturn vexpressionmenu.buildSnippetMenu('attribwrangle/snippet')", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "editor": "1", "editorlang": "VEX", "editorlines": "8-30", "script_action": "import vexpressionmenu\n\nnode = kwargs['node']\nparmname = 'snippet'\n\nvexpressionmenu.createSpareParmsFromChCalls(node, parmname)", "script_action_help": "Creates spare parameters for each unique call of ch() ", "script_action_icon": "BUTTONS_create_parm_from_ch"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("exportlist", "Attributes to Create", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_strict", "Enforce Prototypes", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1_1", "Bindings", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("autobind", "Autobind by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("bindings", "Number of Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindname#", "Attribute Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("groupautobind", "Autobind Groups by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("groupbindings", "Group Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupname#", "Group Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_cwdpath", "Evaluation Node Path", 1, default_value=(["."]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_outputmask", "Export Parameters", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_updatenmls", "Update Normals If Displaced", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_matchattrib", "Attribute to Match", 1, default_value=(["id"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_inplace", "Compute Results In Place", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_selectiongroup", "Output Selection Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_precision", "VEX Precision", 1, default_value=(["auto"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["auto","32","64"]), menu_labels=(["Auto","32-bit","64-bit"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("amount", "Amount", 1, default_value=([0]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/banking/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@N = v@oldnorm;\n\nmatrix3 rot = ident();\nfloat bank_amount = detail(0, \"bank_amount\");\n// rotate(rot, -f@bank_ratio * ch(\"amount\"), @N);\nrotate(rot, -f@bank_ratio * bank_amount, @N);\n\nv@right *= rot;\nv@up *= rot;")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/folder11 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("folder11")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/banking/amount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/banking")
hou_parm = hou_node.parm("amount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.089999999999999997)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/vis_coordinate
hou_node = hou_parent.createNode("visualize", "vis_coordinate", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.65536, -11.0881))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setvisualizers", "Update Visualizers", default_value=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("clearvisualizers", "Clear Incoming Visualizers", default_value=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setvisualizers == 0 }")
hou_parm_template.setTags({"autoscope": "0000000000000000"})
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("wireframe", "Wireframe", menu_items=(["nochange","shaded","viewport","wireframe"]), menu_labels=(["No Change","Force Shaded","Use Viewport Settings","Force Wireframe"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("lit", "Lighting", menu_items=(["nochange","unlit","lit"]), menu_labels=(["No Change","Unlit","Lit"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("xray", "X-Ray", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setcuspangle", "Set Cusp Angle", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("cuspangle", "Cusp Angle", 1, default_value=([60]), min=0, max=180, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setcuspangle == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("showpoints", "Show Points", menu_items=(["nochange","unconnected","all"]), menu_labels=(["No Change","Unconnected","All"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spherepoints", "Points as Spheres", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spriteblend", "Sprite Blending", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setspritecutoff", "Set Sprite Cutoff", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("spritecutoff", "Sprite Cutoff", 1, default_value=([0.5]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setspritecutoff == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("node_vis_enabled", "Visualization Enabled", default_value=True)
hou_parm_template.hide(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("num_visualizers", "Visualizers", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template.hide(True)
hou_parm_template.setTags({"multistartoffset": "0"})
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vis_active#", "Active #", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vis_data#", "Raw Data #", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.hideLabel(True)
hou_parm_template2.setTags({"editor": "1"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/vis_coordinate/setvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("setvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/clearvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("clearvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/wireframe parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("wireframe")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/lit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("lit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/xray parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("xray")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/setcuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("setcuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/cuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("cuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(60)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/showpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("showpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/spherepoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("spherepoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/spriteblend parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("spriteblend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/setspritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("setspritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/spritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("spritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/node_vis_enabled parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("node_vis_enabled")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/num_visualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("num_visualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_active0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_active0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_data0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_data0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("{\n\t\"flags\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":27\n\t},\n\t\"icon\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"VIEW_visualization_color\"\n\t},\n\t\"label\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"right\"\n\t},\n\t\"name\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"right\"\n\t},\n\t\"parameters\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"{\\nversion 0.8\\nstyle\\t[ 0\\tlocks=0 ]\\t(\\t\\\"vector\\\"\\t)\\nclass\\t[ 0\\tlocks=0 ]\\t(\\t\\\"point\\\"\\t)\\nattrib\\t[ 0\\tlocks=0 ]\\t(\\tright\\t)\\nvisibility\\t[ 0\\tlocks=0 ]\\t(\\t\\\"always\\\"\\t)\\ndecorradius\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ngroup\\t[ 0\\tlocks=0 ]\\t(\\t\\\"\\\"\\t)\\npointsize\\t[ 0\\tlocks=0 ]\\t(\\t3\\t)\\nlengthscale\\t[ 0\\tlocks=0 ]\\t(\\t0.47199999999999998\\t)\\nunitlength\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nnormalize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\narrowheads\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\nvectorcoloring\\t[ 0\\tlocks=0 ]\\t(\\t\\\"fixed\\\"\\t)\\ncolorattrib\\t[ 0\\tlocks=0 ]\\t(\\tCd\\t)\\nramptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"false\\\"\\t)\\ncolorramp\\t[ 0\\tlocks=0 ]\\t(\\t5\\t)\\nrangespec\\t[ 0\\tlocks=0 ]\\t(\\t\\\"center-width\\\"\\t)\\nminscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nmaxscalar\\t[ 0\\tlocks=0 ]\\t(\\t10\\t)\\ncenterscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nwidthscalar\\t[ 0\\tlocks=0 ]\\t(\\t2\\t)\\nclamptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"edge\\\"\\t)\\ntreatasscalar\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\nusing\\t[ 0\\tlocks=0 ]\\t(\\t\\\"length\\\"\\t)\\ncomponent\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrefvec\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t)\\nmarkercolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\ntrail\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t0.5\\t)\\ntextcolor\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t0.75\\t0.75\\t)\\nfontsize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"guidefont\\\"\\t)\\nxcolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\nycolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t1\\t)\\nzcolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t1\\t1\\t)\\ncolorramp1pos\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp1c\\t[ 0\\tlocks=0 ]\\t(\\t0.20000000298023224\\t0\\t1\\t)\\ncolorramp1interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp2pos\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t)\\ncolorramp2c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0.85000002384185791\\t1\\t)\\ncolorramp2interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp3pos\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ncolorramp3c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0.10000000149011612\\t)\\ncolorramp3interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp4pos\\t[ 0\\tlocks=0 ]\\t(\\t0.75\\t)\\ncolorramp4c\\t[ 0\\tlocks=0 ]\\t(\\t0.94999998807907104\\t1\\t0\\t)\\ncolorramp4interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp5pos\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncolorramp5c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ncolorramp5interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\n}\\n\"\n\t},\n\t\"scope\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":2\n\t},\n\t\"type\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_marker\"\n\t}\n}\n")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_active1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_active1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_data1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_data1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("{\n\t\"flags\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":27\n\t},\n\t\"icon\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"VIEW_visualization_color\"\n\t},\n\t\"label\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"up\"\n\t},\n\t\"name\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"up\"\n\t},\n\t\"parameters\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"{\\nversion 0.8\\nstyle\\t[ 0\\tlocks=0 ]\\t(\\t\\\"vector\\\"\\t)\\nclass\\t[ 0\\tlocks=0 ]\\t(\\t\\\"point\\\"\\t)\\nattrib\\t[ 0\\tlocks=0 ]\\t(\\tup\\t)\\nvisibility\\t[ 0\\tlocks=0 ]\\t(\\t\\\"always\\\"\\t)\\ndecorradius\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ngroup\\t[ 0\\tlocks=0 ]\\t(\\t\\\"\\\"\\t)\\npointsize\\t[ 0\\tlocks=0 ]\\t(\\t3\\t)\\nlengthscale\\t[ 0\\tlocks=0 ]\\t(\\t0.30399999999999999\\t)\\nunitlength\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nnormalize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\narrowheads\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\nvectorcoloring\\t[ 0\\tlocks=0 ]\\t(\\t\\\"fixed\\\"\\t)\\ncolorattrib\\t[ 0\\tlocks=0 ]\\t(\\tCd\\t)\\nramptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"false\\\"\\t)\\ncolorramp\\t[ 0\\tlocks=0 ]\\t(\\t5\\t)\\nrangespec\\t[ 0\\tlocks=0 ]\\t(\\t\\\"center-width\\\"\\t)\\nminscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nmaxscalar\\t[ 0\\tlocks=0 ]\\t(\\t10\\t)\\ncenterscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nwidthscalar\\t[ 0\\tlocks=0 ]\\t(\\t2\\t)\\nclamptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"edge\\\"\\t)\\ntreatasscalar\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\nusing\\t[ 0\\tlocks=0 ]\\t(\\t\\\"length\\\"\\t)\\ncomponent\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrefvec\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t)\\nmarkercolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t1\\t)\\ntrail\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t0.5\\t)\\ntextcolor\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t0.75\\t0.75\\t)\\nfontsize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"guidefont\\\"\\t)\\nxcolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\nycolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t1\\t)\\nzcolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t1\\t1\\t)\\ncolorramp1pos\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp1c\\t[ 0\\tlocks=0 ]\\t(\\t0.20000000298023224\\t0\\t1\\t)\\ncolorramp1interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp2pos\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t)\\ncolorramp2c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0.85000002384185791\\t1\\t)\\ncolorramp2interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp3pos\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ncolorramp3c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0.10000000149011612\\t)\\ncolorramp3interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp4pos\\t[ 0\\tlocks=0 ]\\t(\\t0.75\\t)\\ncolorramp4c\\t[ 0\\tlocks=0 ]\\t(\\t0.94999998807907104\\t1\\t0\\t)\\ncolorramp4interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp5pos\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncolorramp5c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ncolorramp5interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\n}\\n\"\n\t},\n\t\"scope\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":2\n\t},\n\t\"type\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_marker\"\n\t}\n}\n")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_active2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_active2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vis_coordinate/vis_data2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/vis_coordinate")
hou_parm = hou_node.parm("vis_data2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("{\n\t\"flags\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":27\n\t},\n\t\"icon\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"VIEW_visualization_color\"\n\t},\n\t\"label\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"normal\"\n\t},\n\t\"name\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"normal\"\n\t},\n\t\"parameters\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"{\\nversion 0.8\\nstyle\\t[ 0\\tlocks=0 ]\\t(\\t\\\"vector\\\"\\t)\\nclass\\t[ 0\\tlocks=0 ]\\t(\\t\\\"point\\\"\\t)\\nattrib\\t[ 0\\tlocks=0 ]\\t(\\toldnorm\\t)\\nvisibility\\t[ 0\\tlocks=0 ]\\t(\\t\\\"always\\\"\\t)\\ndecorradius\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ngroup\\t[ 0\\tlocks=0 ]\\t(\\t\\\"\\\"\\t)\\npointsize\\t[ 0\\tlocks=0 ]\\t(\\t3\\t)\\nlengthscale\\t[ 0\\tlocks=0 ]\\t(\\t0.30399999999999999\\t)\\nunitlength\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nnormalize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\narrowheads\\t[ 0\\tlocks=0 ]\\t(\\t\\\"off\\\"\\t)\\nvectorcoloring\\t[ 0\\tlocks=0 ]\\t(\\t\\\"fixed\\\"\\t)\\ncolorattrib\\t[ 0\\tlocks=0 ]\\t(\\tCd\\t)\\nramptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"false\\\"\\t)\\ncolorramp\\t[ 0\\tlocks=0 ]\\t(\\t5\\t)\\nrangespec\\t[ 0\\tlocks=0 ]\\t(\\t\\\"center-width\\\"\\t)\\nminscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nmaxscalar\\t[ 0\\tlocks=0 ]\\t(\\t10\\t)\\ncenterscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nwidthscalar\\t[ 0\\tlocks=0 ]\\t(\\t2\\t)\\nclamptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"edge\\\"\\t)\\ntreatasscalar\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\nusing\\t[ 0\\tlocks=0 ]\\t(\\t\\\"length\\\"\\t)\\ncomponent\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrefvec\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t)\\nmarkercolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t1\\t1\\t)\\ntrail\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t0.5\\t)\\ntextcolor\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t0.75\\t0.75\\t)\\nfontsize\\t[ 0\\tlocks=0 ]\\t(\\t\\\"guidefont\\\"\\t)\\nxcolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\nycolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t1\\t)\\nzcolor\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t1\\t1\\t)\\ncolorramp1pos\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp1c\\t[ 0\\tlocks=0 ]\\t(\\t0.20000000298023224\\t0\\t1\\t)\\ncolorramp1interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp2pos\\t[ 0\\tlocks=0 ]\\t(\\t0.25\\t)\\ncolorramp2c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0.85000002384185791\\t1\\t)\\ncolorramp2interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp3pos\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t)\\ncolorramp3c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0.10000000149011612\\t)\\ncolorramp3interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp4pos\\t[ 0\\tlocks=0 ]\\t(\\t0.75\\t)\\ncolorramp4c\\t[ 0\\tlocks=0 ]\\t(\\t0.94999998807907104\\t1\\t0\\t)\\ncolorramp4interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp5pos\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncolorramp5c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ncolorramp5interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\n}\\n\"\n\t},\n\t\"scope\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":2\n\t},\n\t\"type\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_marker\"\n\t}\n}\n")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/sweep1
hou_node = hou_parent.createNode("sweep::2.0", "sweep1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0384112, -11.5669))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/sweep1/curvegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("curvegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/crosssectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("crosssectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/surface_folder1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("surface_folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/surfaceshape parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("surfaceshape")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ribbon")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/surfacetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("surfacetype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("tris")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/radius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("radius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.10000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/width parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("width")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/reversecrosssections parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("reversecrosssections")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/stretcharoundturns parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("stretcharoundturns")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/maxstretcharoundturns parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("maxstretcharoundturns")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/endcaps_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("endcaps_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/endcaptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("endcaptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/capdivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("capdivs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/triangularpoles parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("triangularpoles")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/capscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("capscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/caproundness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("caproundness")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addendcapsgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addendcapsgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/endcapsgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("endcapsgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("endcaps")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scale_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scale_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/applyscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("applyscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/rotation_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("rotation_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/applyroll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("applyroll")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/roll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("roll")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/fulltwists parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("fulltwists")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/incroll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("incroll")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/rollper parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("rollper")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("fulldistance")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/rollattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("rollattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("roll")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/applyyaw parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("applyyaw")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/yaw parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("yaw")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/incyaw parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("incyaw")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/yawper parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("yawper")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("fulldistance")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/yawattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("yawattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("yaw")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/applypitch parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("applypitch")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/pitch parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("pitch")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/incpitch parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("incpitch")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/pitchper parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("pitchper")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("fulldistance")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/pitchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("pitchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("pitch")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/cross_sections_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("cross_sections_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/copyorder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("copyorder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("each")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/crosssectionattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("crosssectionattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("variant")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/primtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("primtype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/unrollclosedrowcol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("unrollclosedrowcol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/swaprowcol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("swaprowcol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/closeifnocurveinput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("closeifnocurveinput")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/up_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("up_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/upvectortype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("upvectortype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("normal")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/upvectoratstart parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("upvectoratstart")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/useendupvector parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("useendupvector")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/upvectorattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("upvectorattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("start_up")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/endupvectorattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("endupvectorattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("end_up")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/upvector parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm_tuple = hou_node.parmTuple("upvector")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/sweep1/endupvector parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm_tuple = hou_node.parmTuple("endupvector")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/sweep1/tangents_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("tangents_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/tangenttype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("tangenttype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("avgdir")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/continuousclosed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("continuousclosed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/extrapolateendtangents parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("extrapolateendtangents")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/transformbyattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("transformbyattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/uv_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("uv_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/computeuvs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("computeuvs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/overrideexistinguvs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("overrideexistinguvs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/lengthweighteduvs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("lengthweighteduvs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/normalizeu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("normalizeu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/normalizev parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("normalizev")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/flipu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("flipu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/uvscale_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("uvscale_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/uvscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm_tuple = hou_node.parmTuple("uvscale")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/sweep1/usemeshedgelengths parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("usemeshedgelengths")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/propscalepercurve parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("propscalepercurve")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/uvseams_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("uvseams_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/wrapu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("wrapu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/wrapv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("wrapv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/attributes_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("attributes_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/input_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("input_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/attribsfrombackbone parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("attribsfrombackbone")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("* ^P ^N ^up ^pscale ^scale ^orient ^rot ^pivot ^trans ^transform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/attribsfromcrosssection parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("attribsfromcrosssection")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/output_folder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("output_folder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addptrow parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addptrow")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/ptrowattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("ptrowattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ptrow")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addptcol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addptcol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/ptcolattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("ptcolattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ptcol")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addprimrow parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addprimrow")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/primrowattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("primrowattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primrow")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addprimcol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addprimcol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/primcolattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("primcolattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primcol")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addcrosssectionnum parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addcrosssectionnum")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/crosssectionnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("crosssectionnumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("crossnum")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/addcurvenum parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("addcurvenum")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/curvenumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("curvenumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curvenum")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp1pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp1value")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp1interp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("linear")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp2pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp2value")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sweep1/scaleramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sweep1")
hou_parm = hou_node.parm("scaleramp2interp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("linear")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/matchsize1
hou_node = hou_parent.createNode("matchsize", "matchsize1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.3868, -12.6173))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/matchsize1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/justifytarget parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("justifytarget")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/doboundgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("doboundgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/folder2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/sourcegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("sourcegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/sourcegrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("sourcegrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/refgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("refgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/refgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("refgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/folder1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/matchsize1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/matchsize1/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/dotranslate parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("dotranslate")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/justify_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("justify_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/goal_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("goal_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("same")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/offset_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("offset_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/justify_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("justify_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("center")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/goal_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("goal_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("center")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/offset_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("offset_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/justify_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("justify_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/goal_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("goal_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("same")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/offset_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("offset_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/doscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("doscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/uniformscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("uniformscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/scale_axis parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("scale_axis")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/scale_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("scale_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/scale_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("scale_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/scale_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("scale_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/restorexform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("restorexform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/restoreattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("restoreattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/stashxform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("stashxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/stashattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("stashattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/matchsize1/stashmerge parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/matchsize1")
hou_parm = hou_node.parm("stashmerge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("replace")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/uvproject1
hou_node = hou_parent.createNode("uvproject", "uvproject1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.276297, -10.5669))
hou_node.bypass(True)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/uvproject1/uvattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("uvattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uv")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("vertices")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/projtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("projtype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("texture")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/torrad parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("torrad")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.20000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/switcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("switcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((-0.58322155475616455, 0, -5.0020465850830078))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/uvproject1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((90, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/uvproject1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2.4991176128387451, 10.051481246948242, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/uvproject1/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/uvproject1/inittype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("inittype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("best")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/initbbox parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("initbbox")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/urange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("urange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/uvproject1/vrange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm_tuple = hou_node.parmTuple("vrange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/uvproject1/angle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("angle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/fixseams parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("fixseams")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/fixpolar parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("fixpolar")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uvproject1/polerad parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/uvproject1")
hou_parm = hou_node.parm("polerad")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.01)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/resample2
hou_node = hou_parent.createNode("resample", "resample2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.91057, -14.0563))
hou_node.bypass(True)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/resample2/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/maintainprimorder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("maintainprimorder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/lod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("lod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/edge parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("edge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("dist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/measure parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("measure")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/dolength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("dolength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/length parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("length")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.040000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/dosegs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("dosegs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/segs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("segs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/useattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("useattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/allequal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("allequal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/last parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("last")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/randomshift parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("randomshift")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/onlypoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("onlypoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/treatpolysas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("treatpolysas")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("straight")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/outputsubdpoly parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("outputsubdpoly")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/doptdistattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("doptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/ptdistattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("ptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ptdist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/dotangentattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("dotangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/tangentattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("tangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("tangentu")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/docurveuattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("docurveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/curveuattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("curveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curveu")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/docurvenumattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("docurvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/resample2/curvenumattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/resample2")
hou_parm = hou_node.parm("curvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curvenum")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/ray1
hou_node = hou_parent.createNode("ray", "ray1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.333013, -15.4184))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/ray1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/entity parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("entity")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/collision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("collision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("project")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/dirmethod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("dirmethod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("normal")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/dir parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm_tuple = hou_node.parmTuple("dir")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.x", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.x", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.x", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.y", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.y", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.y", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.z", hou.exprLanguage.Hscript)
hou_parm_tuple[2].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.z", hou.exprLanguage.Hscript)
hou_parm_tuple[2].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("@N.z", hou.exprLanguage.Hscript)
hou_parm_tuple[2].setKeyframe(hou_keyframe)


# Code for /obj/geo1/ray1/dirattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("dirattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("N")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/showguide parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("showguide")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/dotrans parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("dotrans")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/lookfar parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("lookfar")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/putnml parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("putnml")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/putdist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("putdist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/reverserays parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("reverserays")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/rtolerance parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("rtolerance")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.01)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/lift parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("lift")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/bias parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("bias")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/maxraydistcheck parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("maxraydistcheck")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/maxraydist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("maxraydist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/sample parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("sample")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/jitter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("jitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/combinetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("combinetype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("average")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/seed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/newgrp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("newgrp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/hitgrp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("hitgrp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("rayHitGroup")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/useprimnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("useprimnumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/primnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("primnumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("hitprim")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/useprimuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("useprimuvwattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/primuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("primuvwattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("hitprimuv")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/getptattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("getptattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/ptattribnames parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("ptattribnames")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/vertexattribnames parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("vertexattribnames")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/primitiveattribnames parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("primitiveattribnames")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ray1/detailattribnames parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ray1")
hou_parm = hou_node.parm("detailattribnames")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/grid1
hou_node = hou_parent.createNode("grid", "grid1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.7809, -13.8174))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/grid1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("zx")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((30, 30))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/grid1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/grid1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/grid1/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(100)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(100)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/orderu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/orderv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/interpu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("interpu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/grid1/interpv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/grid1")
hou_parm = hou_node.parm("interpv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/output0
hou_node = hou_parent.createNode("output", "output0", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.18371, -16.7466))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(True)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/output0/outputidx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/output0")
hou_parm = hou_node.parm("outputidx")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/center_line
hou_node = hou_parent.createNode("python", "center_line", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.4056, 0.708703))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("python", "Python Code", 1, default_value=(["node = hou.pwd()\ngeo = node.geometry()\n\n# Add code to modify contents of geo.\n# Use drop down menu to select examples.\n"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="import pythonscriptmenu\n\nreturn pythonscriptmenu.buildSnippetMenu('Sop/pythonscript/python')", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.setTags({"editor": "1", "editorlang": "python", "editorlines": "20-50"})
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("radial_amp", "Radial_Amplitude", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("height_amp", "Height_Amplitude", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bank_amount", "Bank_Amount", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("order", "Order", 1, default_value=([5]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/center_line/python parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/center_line")
hou_parm = hou_node.parm("python")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("import math\nimport numpy as np\n\nnode = hou.pwd()\ngeo = node.geometry()\n\n# Add code to modify contents of geo.\n# Use drop down menu to select examples.\ng = node.parmTemplateGroup()\np1 = hou.FloatParmTemplate(\"radial_amp\", \"Radial_Amplitude\", 1, default_value=[1])\np2 = hou.FloatParmTemplate(\"height_amp\", \"Height_Amplitude\", 1, default_value=[1])\np3 = hou.FloatParmTemplate(\"bank_amount\", \"Bank_Amount\", 1, default_value=[0])\np4 = hou.IntParmTemplate(\"order\", \"Order\", 1, default_value = [5])\nif(g.find(\"radial_amp\") == None):\n    g.append(p1)\nif(g.find(\"height_amp\") == None):\n    g.append(p2)\nif(g.find(\"bank_amount\") == None):\n    g.append(p3)\nif(g.find(\"order\") == None):\n    g.append(p4)\nnode.setParmTemplateGroup(g)\n\nN = 360\nR = 7\norder = 5\nradial_amp = 0.1*node.parm(\"radial_amp\").eval()\nheight_amp = 0.01*node.parm(\"height_amp\").eval()\nbank_amount = 0.1*node.parm(\"bank_amount\").eval()\norder = node.parm(\"order\").eval()\nR = 2*order\n\ncurve = geo.createNURBSCurve(N+1)\ni = 0\nnode.geometry().addAttrib(hou.attribType.Point, \"N\", (0.1, 0.1, 0.1))\nnode.geometry().addAttrib(hou.attribType.Global, \"bank_amount\", bank_amount)\n# node.geometry().addAttrib(hou.attribType.Global, \"amp\", -1*np.ones(order*2))\n\n# amp = node.geometry().attribValue(\"amp\")\namp = np.random.uniform(-1, 1, order*2)\nheightAmp = np.random.uniform(-1, 1, order*2)\n# node.geometry().addAttrib(hou.attribType.Point, \"curveu\", (0.1, 0.1, 0.1))\nfor vertex in curve.vertices():\n    theta = i/N * 2*math.pi\n    length = R\n    for j in range(3, order):\n        length += radial_amp*(amp[2*j]*math.sin((j+1)*theta) + amp[2*j+1]*math.cos((j+1)*theta))\n        # length = R\n      \n    # delta_length = - 6*radial_amp.sin(theta*6)\n    # k = (length + delta_length*math.tan(theta))/(-length*math.tan(theta)+delta_length)\n    # k_theta = math.atan(k)\n    # dir_x = math.sqrt(1/(1+k*k))\n    # dir_y = math.sqrt(k*k/(1+k*k))\n    \n    # height = height_amp*math.cos(theta*6)\n    for j in range(3, order):\n        height += height_amp*(heightAmp[2*j]*math.sin((j+1)*theta) + heightAmp[2*j+1]*math.cos((j+1)*theta))\n    \n    vertex.point().setPosition((length * math.cos(theta), height, length *math.sin(theta)))\n    Nx = (-6*radial_amp*math.sin(theta*6) * math.cos(theta) - length * math.sin(theta), 0, -6*radial_amp*math.sin(theta*6) * math.sin(theta) + length * math.cos(theta))\n    norm = math.sqrt((Nx[0]*Nx[0] + Nx[1]*Nx[1] + Nx[2]*Nx[2]))\n    Nx = (Nx[0]/norm, Nx[1]/norm, Nx[2]/norm)\n    vertex.point().setAttribValue(\"N\", Nx)\n    i = i + 1\n    ")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/center_line/radial_amp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/center_line")
hou_parm = hou_node.parm("radial_amp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(9.0500000000000007)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/center_line/height_amp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/center_line")
hou_parm = hou_node.parm("height_amp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(8.9800000000000004)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/center_line/bank_amount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/center_line")
hou_parm = hou_node.parm("bank_amount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2.04)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/center_line/order parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/center_line")
hou_parm = hou_node.parm("order")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(7)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/transformed_centerline
hou_node = hou_parent.createNode("matchsize", "transformed_centerline", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.83965, -14.5582))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/transformed_centerline/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/justifytarget parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("justifytarget")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("origin")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/doboundgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("doboundgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/folder2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/sourcegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("sourcegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/sourcegrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("sourcegrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/refgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("refgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/refgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("refgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/folder1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/transformed_centerline/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/transformed_centerline/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/dotranslate parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("dotranslate")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/justify_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("justify_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/goal_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("goal_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("same")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/offset_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("offset_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/justify_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("justify_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("center")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/goal_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("goal_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("same")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/offset_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("offset_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2.0099999999999998)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/justify_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("justify_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/goal_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("goal_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("same")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/offset_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("offset_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/doscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("doscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/uniformscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("uniformscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/scale_axis parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("scale_axis")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/scale_x parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("scale_x")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/scale_y parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("scale_y")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/scale_z parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("scale_z")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/restorexform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("restorexform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/restoreattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("restoreattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xformn")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/stashxform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("stashxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/stashattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("stashattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/transformed_centerline/stashmerge parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/transformed_centerline")
hou_parm = hou_node.parm("stashmerge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("replace")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/ends1
hou_node = hou_parent.createNode("ends", "ends1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.375432, -0.305147))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/ends1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/pshapeu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("pshapeu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/pshapev parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("pshapev")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/closeu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("closeu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("closeround")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/closev parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("closev")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("closeround")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/clampu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("clampu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("sameclamp")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/ends1/clampv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/ends1")
hou_parm = hou_node.parm("clampv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("sameclamp")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/geo1/resample1
hou_node = hou_parent.node("resample1")
if hou_parent.node("ends1") is not None:
    hou_node.setInput(0, hou_parent.node("ends1"), 0)
# Code to establish connections for /obj/geo1/curv_dirs
hou_node = hou_parent.node("curv_dirs")
if hou_parent.node("resample1") is not None:
    hou_node.setInput(0, hou_parent.node("resample1"), 0)
# Code to establish connections for /obj/geo1/bank_ratio
hou_node = hou_parent.node("bank_ratio")
if hou_parent.node("curv_dirs") is not None:
    hou_node.setInput(0, hou_parent.node("curv_dirs"), 0)
# Code to establish connections for /obj/geo1/attribtransfer1
hou_node = hou_parent.node("attribtransfer1")
if hou_parent.node("curv_dirs") is not None:
    hou_node.setInput(0, hou_parent.node("curv_dirs"), 0)
if hou_parent.node("bank_ratio") is not None:
    hou_node.setInput(1, hou_parent.node("bank_ratio"), 0)
# Code to establish connections for /obj/geo1/visualize1
hou_node = hou_parent.node("visualize1")
if hou_parent.node("banking") is not None:
    hou_node.setInput(0, hou_parent.node("banking"), 0)
# Code to establish connections for /obj/geo1/min_ratio
hou_node = hou_parent.node("min_ratio")
if hou_parent.node("attribtransfer1") is not None:
    hou_node.setInput(0, hou_parent.node("attribtransfer1"), 0)
# Code to establish connections for /obj/geo1/max_ratio
hou_node = hou_parent.node("max_ratio")
if hou_parent.node("min_ratio") is not None:
    hou_node.setInput(0, hou_parent.node("min_ratio"), 0)
# Code to establish connections for /obj/geo1/attribremap1
hou_node = hou_parent.node("attribremap1")
if hou_parent.node("max_ratio") is not None:
    hou_node.setInput(0, hou_parent.node("max_ratio"), 0)
# Code to establish connections for /obj/geo1/banking
hou_node = hou_parent.node("banking")
if hou_parent.node("attribremap1") is not None:
    hou_node.setInput(0, hou_parent.node("attribremap1"), 0)
# Code to establish connections for /obj/geo1/vis_coordinate
hou_node = hou_parent.node("vis_coordinate")
if hou_parent.node("banking") is not None:
    hou_node.setInput(0, hou_parent.node("banking"), 0)
# Code to establish connections for /obj/geo1/sweep1
hou_node = hou_parent.node("sweep1")
if hou_parent.node("uvproject1") is not None:
    hou_node.setInput(0, hou_parent.node("uvproject1"), 0)
# Code to establish connections for /obj/geo1/matchsize1
hou_node = hou_parent.node("matchsize1")
if hou_parent.node("sweep1") is not None:
    hou_node.setInput(0, hou_parent.node("sweep1"), 0)
# Code to establish connections for /obj/geo1/uvproject1
hou_node = hou_parent.node("uvproject1")
if hou_parent.node("banking") is not None:
    hou_node.setInput(0, hou_parent.node("banking"), 0)
# Code to establish connections for /obj/geo1/resample2
hou_node = hou_parent.node("resample2")
if hou_parent.node("matchsize1") is not None:
    hou_node.setInput(0, hou_parent.node("matchsize1"), 0)
# Code to establish connections for /obj/geo1/ray1
hou_node = hou_parent.node("ray1")
if hou_parent.node("grid1") is not None:
    hou_node.setInput(0, hou_parent.node("grid1"), 0)
if hou_parent.node("matchsize1") is not None:
    hou_node.setInput(1, hou_parent.node("matchsize1"), 0)
# Code to establish connections for /obj/geo1/output0
hou_node = hou_parent.node("output0")
if hou_parent.node("ray1") is not None:
    hou_node.setInput(0, hou_parent.node("ray1"), 0)
# Code to establish connections for /obj/geo1/transformed_centerline
hou_node = hou_parent.node("transformed_centerline")
if hou_parent.node("center_line") is not None:
    hou_node.setInput(0, hou_parent.node("center_line"), 0)
# Code to establish connections for /obj/geo1/ends1
hou_node = hou_parent.node("ends1")
if hou_parent.node("center_line") is not None:
    hou_node.setInput(0, hou_parent.node("center_line"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

