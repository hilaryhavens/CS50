    def all_aloud_said_text_for_speaker(book_body, who):
        all_text = ""
        for e in book_body.iter("{http://www.tei-c.org/ns/1.0}said"):
            if who not in e.attrib['who']:
                continue
            if 'aloud' not in e.attrib or e.attrib['aloud'] == 'false':
                continue
            for elem in e.iter():
                if elem.text:
                    all_text += ' ' + elem.text
                if elem.tail:
                    all_text += ' ' + elem.tail
        return all_text