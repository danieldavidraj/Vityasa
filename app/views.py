from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from statistics import mean
import itertools

slots=[
    {
        "slot":0,
        "name":[]
    },
    {
        "slot":1,
        "name":[]
    },
    {
        "slot":2,
        "name":[]
    },
    {
        "slot":3,
        "name":[]
    },
    {
        "slot":4,
        "name":[]
    },
    {
        "slot":5,
        "name":[]
    },
    {
        "slot":6,
        "name":[]
    },
    {
        "slot":7,
        "name":[]
    },
    {
        "slot":8,
        "name":[]
    },
    {
        "slot":9,
        "name":[]
    },
    {
        "slot":10,
        "name":[]
    },
    {
        "slot":11,
        "name":[]
    },
    {
        "slot":12,
        "name":[]
    },
    {
        "slot":13,
        "name":[]
    },
    {
        "slot":14,
        "name":[]
    },
    {
        "slot":15,
        "name":[]
    },
    {
        "slot":16,
        "name":[]
    },
    {
        "slot":17,
        "name":[]
    },
    {
        "slot":18,
        "name":[]
    },
    {
        "slot":19,
        "name":[]
    },
    {
        "slot":20,
        "name":[]
    },
    {
        "slot":21,
        "name":[]
    },
    {
        "slot":22,
        "name":[]
    },
    {
        "slot":23,
        "name":[]
    },
]

def add_booking(slot,name):
    if len(slots[slot]["name"])<2:
        slots[slot]["name"].append(name)
        return '{{"status":"confirmed booking for {name} in slot {slot}"}}'.format(name = name, slot = slot)
    else:
        return '{{"status":"slot full, unable to save booking for {name} in slot {slot}"}}'.format(name = name, slot = slot)

def cancel_booking(slot,name):
    if name in slots[slot]["name"]:
        slots[slot]["name"].remove(name)
        return '{{ "status":"canceled booking for {name} in slot {slot}"}}'.format(name = name, slot = slot)
    else:
        return '{{ "status":"no booking for the name {name} in slot {slot}"}}'.format(name = name, slot = slot)
        
@csrf_exempt
def booking(request):
    if request.method == "POST":
        input=json.loads(request.body)
        slot=input["slot"]
        name=input["name"]
        return HttpResponse(add_booking(slot,name))
    elif request.method == "GET":
        return HttpResponse([x for x in slots if len(x["name"])>0])

@csrf_exempt
def cancel(request):
    if request.method == "POST":
        input=json.loads(request.body)
        slot=input["slot"]
        name=input["name"]
        return HttpResponse(cancel_booking(slot,name))

@csrf_exempt
def items(request):
    if request.method == "POST":
        items=json.loads(request.body)
        valid_items=[x for x in items if isinstance(x, (int, float)) and x > 0]
        json_dict =  { 
            "valid_entries":len(valid_items), 
            "invalid_entries":len(items)-len(valid_items), 
            "min":min(valid_items),
            "max":max(valid_items),
            "average":mean(valid_items)
        }
        return HttpResponse(json.dumps(json_dict,indent=4))

def dist_sq(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) +\
           (p[1] - q[1]) * (p[1] - q[1])

def is_square(p1, p2, p3, p4):
    d2 = dist_sq(p1, p2)
    d3 = dist_sq(p1, p3)
    d4 = dist_sq(p1, p4)
 
    if d2 == 0 or d3 == 0 or d4 == 0:   
        return False
 
    if d2 == d3 and 2 * d2 == d4 and \
                    2 * dist_sq(p2, p4) == dist_sq(p2, p3):
        return True
 
    if d3 == d4 and 2 * d3 == d2 and \
                    2 * dist_sq(p3, p2) == dist_sq(p3, p4):
        return True
 
    if d2 == d4 and 2 * d2 == d3 and \
                    2 * dist_sq(p2, p3) == dist_sq(p2, p4):
        return True
    return False

points=[]

@csrf_exempt
def plot(request):
    response=""
    if request.method == "POST":
        input=json.loads(request.body)
        x=input["x"]
        y=input["y"]
        points.append((x, y))
        if len(points)>=4:
            for i in itertools.permutations(points, 4):
                if is_square(i[0],i[1],i[2],i[3]):
                    response='{{"status": "Success {p1} {p2} {p3} {p4}"}}'.format(p1 = i[0],p2 = i[1],p3 = i[2],p4 = i[3])
                    break
            else:
                response='{"status": "accepted"}'    
        else:
            response='{"status": "accepted"}'
        return HttpResponse(response)



