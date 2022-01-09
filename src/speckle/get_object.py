from specklepy.api.credentials import StreamWrapper
from specklepy.api import operations
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account, get_local_accounts
import json
from ladybug_geometry.geometry3d import face, pointvector
from honeybee_radiance import sensorgrid

all_accounts = get_local_accounts() # get back a list
account = get_default_account()

# provide any stream, branch, commit, object, or globals url
wrapper = StreamWrapper("https://speckle.xyz/streams/c029aa9054/commits/bede24795b")

# get an authenticated SpeckleClient if you have a local account for the server
client = wrapper.get_client()
client.authenticate(token=account.token)

# get the specified commit data
commit = client.commit.get(wrapper.stream_id, wrapper.commit_id)

# get an authenticated ServerTransport if you have a local account for the server
transport = wrapper.get_transport()

res = operations.receive(commit.referencedObject, transport)

# tests
print(res.get_dynamic_member_names())

# extracting the vertecies that signify the top of each floor
topFloorPoints = []
allPoints = []
for floor in res['@Floor']:

    # sort slab verteces by z and get top points
    sortedZ = sorted(floor.Vertices, key=lambda k: k["z"])

    for i, value in enumerate(sortedZ):
        if i < len(sortedZ) * 0.5:
            topFloorPoints.append(value)

# extracting verteces for glass surfaces
for glassSurface in res['@Glass']:
    print("corner point lengths")
    # Create a lady bug face from this
    lb_glass_pnts = [pointvector.Point3D(pnt.x,pnt.y,pnt.z) for pnt in glassSurface.Vertices]
    lb_glass_face: face = face.Face3D(lb_glass_pnts)
    lb_glass_face.apertures_by_ratio(ratio = 0.99)
    print(lb_glass_face)    

print("point 0")
print((topFloorPoints[0].x))

testPoint0 = topFloorPoints[0]
testPoint1 = topFloorPoints[1]
testPoint2 = topFloorPoints[2]
testPoint3 = topFloorPoints[3]

testPoints = [testPoint0,testPoint1,testPoint2,testPoint3]

lb_pnts = [pointvector.Point3D(pnt.x,pnt.y,pnt.z) for pnt in testPoints]
lb_face = face.Face3D(lb_pnts)

lb_sg = sensorgrid.SensorGrid.from_face3d("test_sensor_grid",[lb_face],1,1,0.8,False)

#print(lb_sg)





        

