def pascal_triangle(n):
        if n <= 0:
                    return []

                    triangle = [[1]]  # Initialize with the first row [1]

                        for i in range(1, n):
                                    row = [1]  # Start each row with 1

                                            for j in range(1, i):
                                                            # Calculate the current value by summing the two numbers above it
                                                                        value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                                                                                    row.append(value)

                                                                                            row.append(1)  # End each row with 1
                                                                                                    triangle.append(row)

                                                                                                        return triangle

