class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        1.ハッシュマップを用いて、配列に各要素が何回出てきたかを記録する
        2.その配列をイテレートして出現要素が半数以上でるかを確認
        
        ハッシュマップ（ハッシュテーブル）とは
        ・キーと値をペアで格納するデータ構造の一つ
        ・ハッシュ値に変換したキーをインデックスにして配列の要素に値を格納する。
        ・O(1)の時間計算量を持つアルゴリズム
        """
        counter = collections.Counter(nums)
        for num in counter:
            if counter[num] > len(nums)//2:
                return num
