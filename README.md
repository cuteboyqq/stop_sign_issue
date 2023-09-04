# stop_sign_issue
[generate_roadsign_stopsign_images.py](generate_roadsign_stopsign_images.py) This code able to generate stop sign and lane marking at bdd100k dataset images and generate corresponding label.txt for yolo 

### Step 0 : Get Stop Sign ROI  and  lane marking ROI

  You can get stop sign ROI from  coco2017 datasets
  
  You can get lane marking ROI from openlanev2 datasets

### Step 1 : Put Stop Sign ROI into bdd100k image , and add stop sign label into yolo.txt
### Step 2 : Put lane marking ROI into  Step 1 image, and add lane marking label into yolo.txt

![208ad74a-42d618b6](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/885f59ef-4ce9-4be8-9ae6-cb598441a7e0)
![212b5e76-5441e31b](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/08af7e5c-fc1e-4766-8615-53afc350126d)
![214a82d4-49e14c83](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/caa06912-5ef6-45a5-a108-d83150733c6f)
![222d61fa-bdb60cac](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/c2f67a4f-1e85-4ab6-8a3c-3d8aefdaaac8)
![223c02c2-d3ee3e75](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/4ef9651f-c2b1-47d0-8869-41307d93bb61)
![233ec95a-8286e569](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/5ceb137a-47ff-4acd-b5a8-23dd934506da)
![262aa0f6-1847d118](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/806230b6-5400-4cbc-b49e-01d91b5a6dcd)
![261c8d45-81edfc38](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/e830feb7-04bb-4e93-b508-0b9971792d6b)
![257fea9a-969b21ef](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/9d1dff19-4d0b-448a-a70e-9265d2c996a7)
![256e0eae-a624980e](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/8abba3fd-e632-47b1-8a98-8dec3b1a489e)
![250e7595-b14da270](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/c4d849f1-6b03-4377-be70-b5bc5be29b4e)
![249ab9de-106add60](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/ae22f95a-7a64-4681-9c06-af81c4bcc762)
![247a504e-1eb1ccac](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/0d892a75-9bf7-4245-91cf-6925936a5bd9)
![245ddac9-57dc4d91](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/6adad45d-100e-4761-8c95-d8a6d24595e0)
![298c5c58-03e79b22](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/6a868c85-7396-4ea8-be6c-c23513295046)
![298a683c-290dd9c3](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/90365347-676a-4321-8488-7cd3d11de063)
![295bcb61-9e7e9637](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/25c5c0c6-d93f-4750-a9c2-6500be9db8ee)
![293e4359-1a29844a](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/29265e78-7973-4bd6-8e0d-6079f14d43c6)
![291dee4f-174061da](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/087579d4-a57c-4bd7-8a39-e50386626da4)
![290dd65a-23020e7e](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/ac837f86-5325-4eee-9e05-a5dc35ecb66a)
![289af74b-f2c8a214](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/cfafe972-6107-4231-bf99-705ea5fe5eda)
![283a9073-f6615250](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/8ee74d20-4dae-4e96-89c4-da12ee938090)
![282ad270-449af315](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/55b3d04e-91b3-46fb-a8c9-07ff4a9e320c)
![279f4a82-f4a582e1](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/89814fc1-512d-40b7-b741-c318853ead59)
![278f2bc1-b4a0c705](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/089ca740-ed32-4b21-be59-5e409b7b0b8a)
![278f2bc1-956cd61b](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/e36a73cd-f884-45a8-989d-6c382ddbb364)
![274a0490-7d65d208](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/3d1dc223-99e5-4930-868e-b25e6a5129ef)
![272d52f6-8aac36b3](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/483b2754-f30a-4f52-abf3-8df97d651425)
![271cef4e-51a2cab2](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/bfec34ea-835c-41bc-a18c-4a58dd85ce43)
![266a937c-7e0decff](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/5cf3e0ba-ade3-423e-afb9-15b521ce83e5)
![266a937c-3b948235](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/9fbd1961-4376-4833-82c1-3f3252704555)
![265eb1d9-244b50f4](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/a6fdfa11-74af-4c6c-8e24-5a3a516c0e1d)
![265a06e8-7fd61378](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/434842c9-0194-4130-819a-52b2382c92c3)
![264b901b-3d77e117](https://github.com/cuteboyqq/stop_sign_issue/assets/58428559/38feda9a-25e7-4fdc-9f5e-398316ef969d)
