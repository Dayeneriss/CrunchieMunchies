import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter= ',')
#print(calorie_stats)
#There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition?
average_calories = np.mean(calorie_stats)
#print(average_calories)

#Does the average calorie count adequately reflect the distribution of the dataset? 
calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

#On dirait que la majorit des crales sont suprieures  la moyenne. Voyons si la mdiane est un meilleur reprsentant de l'ensemble de donnes.
nth_median = np.median(calorie_stats)
#print(nth_median)
"""On cherche  connaitre le plus petit percentile, suprieur  60 car cela permet de montrer qu'une partie importante des concurrents  un nombre de calories suprieur  notre socit."""
print np.percentile(calorie_stats, 3)
print np.percentile(calorie_stats, 3.35)
print np.percentile(calorie_stats, 3.6)
print np.percentile(calorie_stats, 3.7)
#nth_percentile = 3.35
Le plus petit percentile, suprieur  60 est 3.35

# let's calculate the percentage of cereals that have more than 60 calories per serving : 
more_calories = np.mean(calorie_stats > 60)* 100
print(more_calories)

#how much variation exists in the dataset? Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
calorie_std = np.std(calorie_stats)
print(calorie_std)
