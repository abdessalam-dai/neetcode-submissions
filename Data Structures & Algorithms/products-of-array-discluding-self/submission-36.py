class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [nums[0]] + [1 for _ in range(len(nums)-1)]
        suffix_products = [1 for _ in range(len(nums)-1)] + [nums[-1]]
        
        
        for i in range(1, len(nums)):
            print(i)
            prefix_products[i] = prefix_products[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            print(i)
            suffix_products[i] = suffix_products[i+1] * nums[i]

        print(prefix_products)
        print(suffix_products)

        products = []
        for i in range(len(nums)):
            p, s = suffix_products[i], prefix_products[i]
            if i == 0:
                products.append(suffix_products[i+1])
            elif i == len(nums) - 1:
                products.append(prefix_products[i-1])
            else:
                products.append(prefix_products[i-1] * suffix_products[i+1])
        return products
