class Nums:
    list_no_numbers = []

    def remove_number(self, nums, number):
        nums.remove(number)
        for i in nums:
            self.list_no_numbers.append(i)
        print(self.list_no_numbers)

    def missing_number(self, nums):
        for i in nums:
            if nums[i] != self.list_no_numbers[i]:
                return i
