def reward_function(params):
    # Read input parameters
  
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']

    
    if is_offtrack or is_reversed:
        return 0.1

    reward = speed*10

    

    if is_left_of_center == True: 
        reward += distance_from_center*8 

    else:
        reward -= distance_from_center*5 

    steps = params['steps']
    progress = params['progress']

    TOTAL_NUM_STEPS = 200

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 5


    return float(reward)
