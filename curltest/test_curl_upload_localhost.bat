set UPLOAD_API="http://127.0.0.1:8000/api/v1/objectdetection/image"

cd test_images\input\

curl -X POST %UPLOAD_API% -F "image=@image.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__blur4.0.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__fliph.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__rot180.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__zoom200_0_300_300.jpg"

pause

