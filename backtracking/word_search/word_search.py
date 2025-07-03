class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board_replica = board[:]
        def first_match(row , col):
            for row_index in range(row, len(board_replica)):
                for col_index in range(col, len(board_replica[row_index])):
                    word_char = word[0]
                    curr_char= board_replica[row_index][col_index]
                    if word_char==curr_char:
                        return [row_index , col_index , 1, word[0] ]
            return []
        def is_right_path(row, column , word_part , right_path):
            if column!=0  and board_replica[row][column-1] != 0 and right_path+board_replica[row][column-1]==word_part:
                return [row, column-1 , right_path+board_replica[row][column-1] ]
            elif column+1 < len(board_replica[row]) and right_path+board_replica[row][column + 1] == word_part:
                return [row, column+1 , right_path+board_replica[row][column + 1] ]
            elif row+1 < len(board_replica) and right_path+board_replica[row+1][column] == word_part:
                return [row+1, column , right_path+board_replica[row+1][column] ]
            elif row-1 >= 0 and right_path+board_replica[row-1][column] == word_part:
                return [row-1, column , right_path+board_replica[row-1][column] ]
            else :
                return []

        def search(row, column , word_index ,right_path ):
            if right_path=='':
                first_result =first_match(row, column)
                if first_result:
                    row, column,word_index ,right_path=first_result
                else:
                    return

            if right_path==word:
                return True

            for row_index in range(row , len(board_replica)):
                for col_index in range(column , len(board_replica[row_index])):
                    word_part=right_path+word[word_index]
                    next_step=is_right_path(row_index, column , word_part , right_path)
                    if next_step:
                        #issues is here
                        board_replica[row_index][column]=0
                        row_val, next_column, updt_right_path = next_step
                        row_val = row_val if row_val>=row_index else row_index
                        return search(row_val, next_column , word_index+1 ,updt_right_path )
                    else :
                        if right_path==word[0]:
                            return search(row_index, col_index+1 , 0 ,'' )
                        break
                # row_val, column_val, word_index, right_path = first_match(row_index, column+1)
                # search(row_val, column_val, word_index, right_path)

        result = search(0, 0, 0, '')
        return result if result else False
sol= Solution()
# input_list =[
#     ["A", "B", "C", "E"],
#      ["S", "F", "C", "S"],
#      ["A", "D", "E", "E"]
# ]
# print(sol.exist(input_list, 'ABCCED') )
#
# input_list =[
#     ["A","B","C","E"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ]
# print(sol.exist(input_list, 'SEE') )


# input_list =[
#     ["A","B","C","E"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ]
# print(sol.exist(input_list, 'ABCB') )

input_list =[
    ['a','b'],
    ['c','d']
]
print(sol.exist(input_list, 'cdba') )
