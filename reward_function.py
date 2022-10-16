def reward_function(params):
  
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']

    
    if is_offtrack or is_reversed:
        return 0

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    reward = speed*100

    if distance_from_center <= marker_1:
        reward += 100
    elif distance_from_center <= marker_2:
        reward += 50
    elif distance_from_center <= marker_3:
        reward += 10
    else:
        reward = 0  

    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8


    return reward