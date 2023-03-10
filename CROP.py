import laspy
import numpy as np


def main():
    xmin = 191952.00
    ymin = 325070.00
    width = 500
    height = 500
    num_of_points = 50000000
    with laspy.open("./data/pointcloud/C_68GZ1.LAZ") as f:
        with laspy.open("./data/pointcloud/roi.laz", mode="w", header=f.header) as writer:
            for points in f.chunk_iterator(num_of_points):
                X_in_valid = (xmin <= points.x) & (xmin + width >= points.x)
                Y_in_valid = (ymin <= points.y) & (ymin + height >= points.y)
                good_indices = np.where(X_in_valid & Y_in_valid)
                good_indices = good_indices[0].ravel()
                good_points = points[good_indices].copy()
                writer.write_points(good_points)
                print("done")


if __name__ == '__main__':
    main()
