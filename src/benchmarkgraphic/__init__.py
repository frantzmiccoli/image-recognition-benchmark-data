import pandas
import seaborn
from matplotlib import pyplot

from get_data_points_from_line import get_data_points_from_line

### Begin: loading
measured_excel_filepath = './measured.xlsx'
excel = pandas.ExcelFile(measured_excel_filepath)

sheets = excel.sheet_names

data_points = []
for sheet in sheets:
    if sheet == 'porn':
        continue

    data_frame = excel.parse(sheet, 5)

    for row in data_frame.iterrows():
        data_points += get_data_points_from_line(sheet, row)
### End: loading


services = ['Amazon', 'Google', 'Microsoft', 'Clarifai']

services_colors = {
    'Amazon': 'yellow',
    'Google': 'red',
    'Microsoft': 'blue',
    'Clarifai': 'purple'
}
def get_color(item):
    service = item['service']
    return services_colors[service]

def get_service(item):
    return item['service']

sheets.append('global')
sheets.remove('porn')


for sheet in sheets:

    for service in services:
        synthesis = {
            'signal_noise_score': 0,
            'match_score': 0
        }
        count = 0
        for data_point in data_points:

            if (data_point['service'] == service) &\
                    (data_point['base'] == sheet):
                count += 1
                synthesis['signal_noise_score'] +=\
                    data_point['signal_noise_score']
                synthesis['match_score'] += data_point['match_score']


        if count == 0:
            continue

        synthesis['signal_noise_score'] /= float(count)
        synthesis['match_score'] /= float(count)

        xs = [synthesis['signal_noise_score']]
        ys = [synthesis['match_score']]

        color = services_colors[service]
        label = service
        pyplot.scatter(xs, ys, c=color, label=label, alpha=0.7)
        pyplot.annotate(service, (xs[0] + 0.01, ys[0] + 0.01))

    pyplot.grid(True)
    pyplot.axis([0,5,0,5])
    pyplot.xlabel('Signal over noise score')
    pyplot.ylabel('Correct labeling score')
    title = sheet[0].upper() + sheet[1:] + ' dataset'
    pyplot.suptitle(title)
    pyplot.savefig('benchmark-' + sheet + '.png')

    pyplot.close()





