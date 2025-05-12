class hunam_body:
    def __init__(self,eye,mouth,nose):
        self.eye = eye
        self.mouth = mouth
        self.nose = nose
    def show(self):
        print(f"Eye: {self.eye} Mouth: {self.mouth} Nose: {self.nose}")
Ankit=hunam_body(2,3,9)
ayush=hunam_body(6,6,9)
abhay=hunam_body(6,6,8)
Ankit.show()
ayush.show()
abhay.show()