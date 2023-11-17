SELECT characters.name, speeches.text FROM (speeches INNER JOIN characters ON speeches.charID = characters.id);
