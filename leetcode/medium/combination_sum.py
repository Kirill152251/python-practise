import itertools

def combinationSum_my_solution(candidates: list[int], target: int) -> list[list[int]]:
    agregat = []
    sol = []
    for i in range(1, int(target/min(candidates))+1):
        [agregat.append(list(item)) for item in itertools.combinations_with_replacement(candidates, i)]
    
    [sol.append(item) for item in agregat if sum(item) == target]
    for item in candidates:
        if target % item == 0:
            rep = int(target / item)
            temp = [item for _ in range(rep)]
            if temp not in sol:
                sol.append(temp)
    return sol

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    sol = []

    def make_comb(index, comb, total):
        if total == target:
            sol.append(comb[:])
            return
        if index >= len(candidates) or total > target:
            return
        comb.append(candidates[index])
        make_comb(index, comb, total + candidates[index])
        comb.pop()
        make_comb(index+1, comb, total)
        return sol

    return make_comb(0, [], 0)


print(combinationSum([7,3], 17))