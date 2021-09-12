class Solution:
    def longestCommonPrefix(candidates: list):
        common_prefix = ""

        if candidates == []:
            return common_prefix

        for index, reference_letter in enumerate(candidates[0]):
            for potential_match_strings_index in range(1, len(candidates)):
                try:
                    if candidates[potential_match_strings_index][index] != reference_letter:
                        return common_prefix
                except IndexError:
                    break

                if (potential_match_strings_index == len(candidates)-1):
                    common_prefix = common_prefix + reference_letter

        return common_prefix
