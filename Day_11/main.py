def volume_of_figure_a_and_b(a,b,c):
    """
    This win sum all the input and return the result
    """
    answer = a * b * c
    return answer

def volume_of_composit_solid(result):
    result = result / 2
    return result

def volume_of_meter_box(result, composit_solid):
    result = result + composit_solid
    return result

def conver_to_cubic_meter(box_volume):
    output = box_volume / 1000
    return output

result = volume_of_figure_a_and_b(16, 14, 10)
composit_solid = volume_of_composit_solid(result)
box_volume = volume_of_meter_box(result, composit_solid)
convert = conver_to_cubic_meter(box_volume)
print(result)
print(composit_solid)
print(box_volume)
print(convert)