def max_subsequence(D,S):
    D = sorted(D, key=lambda k: len(k), reverse=True)
    for entry in D:
        counter = 0
        matches = 0
        for e in entry:
            while counter < len(S):
                if S[counter] == e:
                    matches += 1
                    counter +=1
                    break

                counter +=1

            if matches == len(entry):
                return entry

            if counter == len(S):
                break

    return None