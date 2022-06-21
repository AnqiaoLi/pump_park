# pump_park

This repository shows how to construct track files in .msgpack with Houdini.

## Installation
First, find which python is used in Houdini, please refer to this link: https://www.sidefx.com/docs/houdini/hom/index.html 

Install the msgpack under this python, in my case:

```bash
/opt/hfs19.0.589/houdini/python/bin/python3.7 -m pip install msgpack
```

## Construct tracks from Houdini 
- In Houdini, construct your own model or choose File/Open... to open the example file pump_track_random.hipnc
- Add a node to save the model as code. If you use pump_track_random.hipnc, you can find a node save_as_code. By running this node, it will automatically generate a file named track_construction.py.
- Setup the Houdini environment outside Houdini:
  ```bash
  cd /opt/hfs19.0.589
  source houdini_setup
  ```
  Then run the file construction_with_houdini.py to generate track files.

## Houdini Model

The centerline of the track in pump_track_random.hipnc is expressed by cylindrical coordinate:
$$
\begin{aligned}
\rho &= radial\_ amp * (\sum _{k=3}^{order} a_k\sin(k\theta) + b_k\cos(k\theta))\\
z &= height\_ amp * (\sum _{k=3}^{order} c_k\sin(k\theta) + d_k\cos(k\theta))
\end{aligned}
$$
$a_k,b_k,c_k,d_k$ are randomly generated in [-1, 1]. $order, radial\_amp, height\_amp$ are adjustable parameters. In additon, bank_ratio is also adjustable which is used when sweeping the centerline to the track surface.

The track is stored in the node /obj/geo1/ray1, the centerline is stored in /obj/geo1/transformed_centerline.

