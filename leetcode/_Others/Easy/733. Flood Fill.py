from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        DFS approach

        v = Vertices
        e = Edges
        d = Depth

        Time complexity:  O(v + e)
        Space complexity: O(d)
        """
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image, sr, sc, source_color, new_color):
        out_of_bounds = sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr])
        if out_of_bounds or image[sr][sc] != source_color or image[sr][sc] == new_color:
            return

        image[sr][sc] = new_color
        self.fill(image, sr + 1, sc, source_color, new_color)
        self.fill(image, sr - 1, sc, source_color, new_color)
        self.fill(image, sr, sc + 1, source_color, new_color)
        self.fill(image, sr, sc - 1, source_color, new_color)
