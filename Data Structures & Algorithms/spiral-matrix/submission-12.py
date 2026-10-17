class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        horiz = 0
        vertic = 0

        left_bound = -1
        top_bound = -1
        right_bound = len(matrix[0])
        bottom_bound = len(matrix)

        curr = 0
        total = right_bound * bottom_bound
        result = []

        while (curr < total):
            
            # Go right
            while (left_bound < vertic and vertic < right_bound and curr < total):
                result.append(matrix[horiz][vertic])
                vertic += 1
                curr += 1
            
            top_bound += 1
            vertic -= 1
            horiz += 1
                
            # Go down
            while (top_bound < horiz and horiz < bottom_bound and curr < total):
                result.append(matrix[horiz][vertic])
                horiz += 1
                curr += 1

            horiz -= 1
            vertic -= 1
            right_bound -= 1

            # Go to the left
            while (left_bound < vertic and vertic < right_bound and curr < total):
                result.append(matrix[horiz][vertic])
                vertic -= 1
                curr += 1


            vertic += 1
            horiz -= 1
            bottom_bound -= 1
                        
            # Go up
            while (top_bound < horiz and horiz < bottom_bound and curr < total):
                result.append(matrix[horiz][vertic])
                horiz -= 1
                curr += 1

            horiz += 1
            vertic += 1
            left_bound += 1

        return result

        