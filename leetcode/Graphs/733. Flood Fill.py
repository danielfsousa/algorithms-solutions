

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """
        Depth first search

        r = number of rows
        c = number of columns

        Time complexity:  O(r * c)
        Space complexity: O(r * c)
        """
        def fill(image, sr, sc, old_color, new_color):
            rows, cols = len(image), len(image[0])
            is_in_bounds = 0 <= sr < rows and 0 <= sc < cols
            if is_in_bounds and image[sr][sc] == old_color:
                image[sr][sc] = new_color
                fill(image, sr - 1, sc, old_color, new_color)
                fill(image, sr + 1, sc, old_color, new_color)
                fill(image, sr, sc - 1, old_color, new_color)
                fill(image, sr, sc + 1, old_color, new_color)
            return image

        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        return fill(image, sr, sc, old_color, newColor)
