set UPLOAD_API="http://127.0.0.1:8000/api/v1/objectdetection/image"
::set UPLOAD_API="https://richmondu.com/api/v1/objectdetection/image"

cd test_images\input\

curl -H "Content-Type: multipart/form-data" -X POST %UPLOAD_API% -F "image=@image.jpg" 
curl -H "Content-Type: multipart/form-data" -X POST %UPLOAD_API% -F "image=@image__blur4.0.jpg" 
curl -H "Content-Type: multipart/form-data" -X POST %UPLOAD_API% -F "image=@image__fliph.jpg" 
curl -H "Content-Type: multipart/form-data" -X POST %UPLOAD_API% -F "image=@image__rot180.jpg" 
curl -H "Content-Type: multipart/form-data" -X POST %UPLOAD_API% -F "image=@image__zoom200_0_300_300.jpg"

pause

