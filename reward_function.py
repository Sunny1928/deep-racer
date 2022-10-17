def reward_function(params):
  
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']

    
    if is_offtrack or is_reversed:
        return 0.1

    reward = speed*80

    distance_from_left = track_width/2 - distance_from_center

    track_width_high = track_width/2*0.25
    track_width_low = track_width/2*0.75

    if is_left_of_center == True:
        if distance_from_left >= track_width_high and distance_from_left <= track_width_low:
            reward += 100
        else:
            reward += 50  
    else:
        reward = 0.1

    return float(reward)
