class Solution_working:
    def repeatedStringMatch(self, A, B):
        if len(A) > len(B):
                if B in A:
                        return 1
                elif B in (A + A):
                        return 2
                else:
                        return -1

        else:
                new_A = A
                counter = 1
                while len(new_A) <= len(B) + 2*len(A):
                        # print("new_A:{}".format(new_A))
                        # print("len(A)+len(B): {}; len(new_A):{}".format(len(B)+len(A),len(new_A)))
                        if B in new_A:
                                return counter
                        counter += 1
                        new_A += A
                return -1


class Solution_working2:
    def repeatedStringMatch(self, A, B):
        if len(A) > len(B):
            if B in A:
                return 1
            elif B in (A + A):
                return 2
            else:
                return -1

        else:
            new_A = A
            counter = 1
            while len(new_A) < len(B):
                counter += 1
                new_A += A
                # print("new_A:{}".format(new_A))
                # print("len(A)+len(B): {}; len(new_A):{}".format(len(B)+len(A),len(new_A)))
            # print(new_A)
            # print(counter)
            # print(B)
            #if A < B, then B in A will be successfull when B and A are atleast of same length, A is len_B + A, or A is len_B + A+A
            for i in range(0, 3):

                if B in new_A:
                    return counter
                new_A += A
                counter += 1

            return -1