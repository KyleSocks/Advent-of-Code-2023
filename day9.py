def get_next(nums:list[int])->int:
    if sum(nums) == 0:
        return 0
    else:
        dxs = []
        for i in range(len(nums) - 1):
            dxs.append(nums[i+1] - nums[i])
        return nums[-1] + get_next(dxs)

def get_prior(nums:list[int])->int:
    if len(set(nums)) == 1:
        return nums[0]
    else:
        dxs = []
        for i in range(len(nums) - 1):
            dxs.append(nums[i+1] - nums[i])
        return nums[0] - get_prior(dxs)


def main():
    file = open('input.txt').read().strip()
    lines = file.split('\n')

    next_nums = []
    prior_nums = []
    for line in lines:
        nums = [int(x) for x in line.strip().split(' ')]
        next_nums.append(get_next(nums))
        prior_nums.append(get_prior(nums))
    print(sum(next_nums))
    print(sum(prior_nums))
    return 0

if __name__ =='__main__':
    main()