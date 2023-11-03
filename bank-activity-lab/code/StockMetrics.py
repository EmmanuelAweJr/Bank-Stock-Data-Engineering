
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            averages.append(round(sum(new_data)/len(new_data),3))
        print(averages)
        return averages


    def median02(self):
        """pt2
        """
        averages = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            averages.append(stats.median(new_data))
        print(averages)
        return averages

    def stddev03(self):
        """pt3
        """
        averages = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            averages.append(round(stats.stdev(new_data),3))
        print(averages)
        return averages
