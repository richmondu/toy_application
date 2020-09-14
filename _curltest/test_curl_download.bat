set DOWNLOAD_API="https://richmondu.com/api/v1/objectdetection/image"

cd test_images\output\

curl -o image.jpg %DOWNLOAD_API%/image.jpg/processed
curl -o image__blur4.jpg %DOWNLOAD_API%/image__blur4.0.jpg/processed
curl -o image__fliph.jpg %DOWNLOAD_API%/image__fliph.jpg/processed
curl -o image__rot180.jpg %DOWNLOAD_API%/image__rot180.jpg/processed
curl -o image__zoom200_0_300_300.jpg %DOWNLOAD_API%/image__zoom200_0_300_300.jpg/processed

pause

