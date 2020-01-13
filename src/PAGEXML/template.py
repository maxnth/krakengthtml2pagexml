SKELETHON = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?><PcGts 
xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2017-07-15" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2017-07-15 
http://schema.primaresearch.org/PAGE/gts/pagecontent/2017-07-15/pagecontent.xsd">{_metadata}{_content}</PcGts>'''.replace('\n', ' ').replace('\r', '')

METADATA = '<Metadata><Creator/><Created>{_time}</Created><LastChange>{_time}</LastChange><Comments/></Metadata>'.replace('\n', ' ').replace('\r', '')

PAGE = '<Page imageFilename="{_img_name}" imageHeight="{_img_height}" imageWidth="{_img_width}">{_content}</Page>'.replace('\n', ' ').replace('\r', '')

READINGORDER = '<ReadingOrder><OrderedGroup id="r0">{regions}</OrderedGroup></ReadingOrder>'.replace('\n', ' ').replace('\r', '')

TEXTREGION = '<TextRegion id="{_id}" type="{_type}"><Coords points="{_points}"/>{_text_lines}</TextRegion>'.replace('\n', ' ').replace('\r', '')

TEXTLINE = '''<TextLine id="{_id}"><Coords points="{_points}"/><TextEquiv index="0"><Unicode>
{_text}</Unicode></TextEquiv></TextLine>'''.replace('\n', ' ').replace('\r', '')
