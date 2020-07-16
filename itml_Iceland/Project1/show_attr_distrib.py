import matplotlib.pyplot as plt
import random

def class_distribution(y_train, y_test):
	f, ax = plt.subplots(1)
	bar_width = 1
	bar_positons = [0, 1]
	tick_pos = [i+(bar_width/2) for i in bar_positons]
	ax.set_xticks(tick_pos)
	ax.set_xticklabels(["train", "test"])
	ax.set_ylabel("Percentages")
	ax.set_xlabel("")
	ax.set_title("Classes")
	ax.set_ylim(0, 100)

	classes_train = y_train.value_counts(normalize=True)
	classes_test = y_test.value_counts(normalize=True)

	bottom = [0, 0]
	for cl in classes_train.index.tolist():
		train_value = classes_train[cl] * 100
		test_value = classes_test[cl] * 100
		ax.bar(bar_positons,
			[train_value, test_value],
			label=cl,
			bottom=bottom,
			color="#%06x" % random.randint(0, 0xFFFFFF),
			width=bar_width,
			edgecolor="#ffffff")
		bottom[0] += train_value
		bottom[1] += test_value
	plt.show()

def grid_of_plots(attributes, X_train, X_test):
	grid_of_plots_size = 5
	bar_width = 1
	bar_positons = [0, 1]
	tick_pos = [i+(bar_width/2) for i in bar_positons] 
	f, ax_array = plt.subplots(grid_of_plots_size, grid_of_plots_size, figsize=(10, 8))
	count_plots_y = 0
	count_plots_x = 0

	for attr in attributes:
		# get occurrences of each attribute value
		unique_values_train = X_train[attr].value_counts(normalize=True)
		unique_values_test = X_test[attr].value_counts(normalize=True)
		num_unique_values = len(unique_values_train)
		
		# some settings for plots
		current_ax = ax_array[count_plots_y, count_plots_x]
		current_ax.set_xticks(tick_pos)
		current_ax.set_xticklabels(["train", "test"])
		current_ax.set_ylabel("")
		current_ax.set_xlabel("")
		current_ax.set_title(attr)
		current_ax.set_ylim(0, 100)
		current_ax.yaxis.set_visible(False)

		# draw subplots
		bottom = [0, 0]
		for value in unique_values_train.index.tolist():
			try:
				train_value = unique_values_train[value] * 100
				test_value = unique_values_test[value] * 100
			except:
				print("ERR: No records with {} as attribute value in one of the sets".format(value))

			current_ax.bar(bar_positons,
				[train_value, test_value],
				label=value,
				bottom=bottom,
				color="#%06x" % random.randint(0, 0xFFFFFF),
				width=bar_width,
				edgecolor="#ffffff")
			bottom[0] += train_value
			bottom[1] += test_value

		count_plots_y += 1
		if (count_plots_y >= grid_of_plots_size):
			count_plots_y = 0
			count_plots_x += 1

	# delete empty plots
	for i in range(count_plots_y, grid_of_plots_size):
		f.delaxes(ax_array[i, count_plots_x])

	plt.subplots_adjust(hspace=0.5)
	plt.show()
