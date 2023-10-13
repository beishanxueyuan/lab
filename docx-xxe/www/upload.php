<?php
if ($_FILES["file"]["error"] > 0)
{
    echo "错误：" . $_FILES["file"]["error"] . "<br>";
}
else
{
    $docx_path="/var/www/html/uploads/".$_FILES["file"]["name"];
    move_uploaded_file($_FILES["file"]["tmp_name"],$docx_path);
    echo "文件url：/uploads/".$_FILES["file"]["name"]."<br>";
    $result=file_get_contents("zip://" . $docx_path . "#word/document.xml");

    $doc = new DOMDocument();
    $doc->loadxml($result, LIBXML_NOENT);
    //获取标签对象
    $book=$doc->getElementsByTagName("body");
    //输出第一个中的值
    echo $book->item(0)->nodeValue;
}
?>