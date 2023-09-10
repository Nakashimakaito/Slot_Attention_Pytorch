# Slot_Attention_Pytorch
pytorchでのslot_Attention[1]の実装。

＊コードのバグあり修正中。

## 現段階の例

slot: それぞれのslot内（slot数: 7）で検知された物体。epochが少ない（300）からか、まだ微妙。

![slot1](image/slot1.png) ![slot2](image/slot2.png) ![slot3](image/slot3.png) ![slot4](image/slot4.png) ![slot5](image/slot5.png) ![slot6](image/slot6.png) ![slot7](image/slot7.png) 

正解画像：

![true](image/true.png)

各slotより再現された画像： 

![reacon](image/reacon.png)

引用論文
[1]Locatello, Francesco, et al. "Object-centric learning with slot attention." Advances in Neural Information Processing Systems 33 (2020): 11525-11538.

参考コード
https://github.com/google-research/google-research/tree/master/slot_attention
