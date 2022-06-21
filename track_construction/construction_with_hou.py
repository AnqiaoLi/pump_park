import msgpack

# To access hou module from a regular python file, see https://www.sidefx.com/docs/houdini/hom/commandline.html
def enableHouModule():
    '''Set up the environment so that "import hou" works.'''
    import sys, os

    # Importing hou will load Houdini's libraries and initialize Houdini.
    # This will cause Houdini to load any HDK extensions written in C++.
    # These extensions need to link against Houdini's libraries,
    # so the symbols from Houdini's libraries must be visible to other
    # libraries that Houdini loads.  To make the symbols visible, we add the
    # RTLD_GLOBAL dlopen flag.
    if hasattr(sys, "setdlopenflags"):
        old_dlopen_flags = sys.getdlopenflags()
        sys.setdlopenflags(old_dlopen_flags | os.RTLD_GLOBAL)

    try:
        import hou
    except ImportError:
        # If the hou module could not be imported, then add 
        # $HFS/houdini/pythonX.Ylibs to sys.path so Python can locate the
        # hou module.
        sys.path.append(os.environ['HHP'])
        import hou
    finally:
        # Reset dlopen flags back to their original value.
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)

# Return positions from Geometry
def getGeoPoints(geo):
    # Exchange axis y and z
    positions = [[i.position().x(),i.position().z(),i.position().y()]  for i in geo.iterPoints()]
    return positions
    
# Save track and centerline from Houdini model
def savePos(outfile_path):
    trackGeo = hou.node('/obj/geo1/ray1').geometry() 
    centerGeo= hou.node('/obj/geo1/transformed_centerline').geometry()
    data = {'positions': getGeoPoints(trackGeo), 'center_line': getGeoPoints(centerGeo)}

    with open(outfile_path, "wb") as outfile:
        packed = msgpack.packb(data)
        outfile.write(packed)


enableHouModule()
import hou

exec(open("/home/anqiao/PumpPark/track_construction/track_constuction.py").read())
outdir = "/home/anqiao/PumpPark/track_construction/tracks"
radial_amp = [1, 6, 11, 16]
height_amp = [0, 3, 6, 9]
bank_amount = [0, 2, 4, 6]
order = 5
rand_num = 10

terrain_difficulties = [(i, j, k) for i in radial_amp for j in height_amp for k in bank_amount]
for i in range(rand_num):
    # Houdini will re-execute the network after updating the parameters
    hou.parm('/obj/geo1/center_line/order').set(order, follow_parm_reference=True)
    for ra, ha, ba in terrain_difficulties:
        hou.parm('/obj/geo1/center_line/radial_amp').set(ra, follow_parm_reference=True)
        hou.parm('/obj/geo1/center_line/height_amp').set(ha, follow_parm_reference=True)
        hou.parm('/obj/geo1/center_line/height_amp').set(ba, follow_parm_reference=True)

        outfile_path = outdir + "/rand_"+str(i)+"_track_ra="+str(ra)+"_ha="+str(ha)+"_ba="+str(ba)
        savePos(outfile_path)



