# import numpy as np
# from sklearn.metrics.pairwise import haversine_distances
# from math import radians
# import pandas as pd
# from uk_covid19 import Cov19API
# # Let's assume we have the following data
# locations = {
#     'London': (51.509865, -0.118092),
#     'Manchester': (53.483959, -2.244644),
#     'Birmingham': (52.489471, -1.898575),
#     'Leeds': (53.801277, -1.548567),
#     'Glasgow': (55.86515, -4.25763)
# }

# # Convert latitude/longitude to radians
# locations_rad = {k: (radians(v[0]), radians(v[1])) for k, v in locations.items()}

# # Create a matrix of all locations
# matrix = np.array(list(locations_rad.values()))

# # Calculate haversine distances
# distances = haversine_distances(matrix, matrix)

# # Convert to kilometers
# distances *= 6371000/1000  # multiply by Earth radius to get kilometers

# print(distances)