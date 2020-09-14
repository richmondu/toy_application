set UPLOAD_API="https://richmondu.com/api/v1/objectdetection/image"

cd test_images\input\

curl -X POST %UPLOAD_API% -F "image=@image.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__blur4.0.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__fliph.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__rot180.jpg" 
curl -X POST %UPLOAD_API% -F "image=@image__zoom200_0_300_300.jpg"

pause

