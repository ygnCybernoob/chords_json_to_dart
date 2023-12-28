import json

def process():

    with open('ukulele.json', 'r') as f:
        raw = f.read()

        js = json.loads(raw)

        data = ''

        fmt1 = "'{0}': [{1}],"
        for i in js['chords']:
            
            fmt2 = "Chord(name: '{0}{1}', chordKey: '{0}', suffix: '{1}', chordPositions: [{2}],),"
            chord = ''
            for j in js['chords'][i]:

                
                fmt3 = "ChordPosition(baseFret: {2}, frets: '{0}', fingers: '{1}',),"
                
                position=''
                for k in j['positions']:
                    frets = ' '.join([str(x) for x in k['frets']])
                    fingers = ' '.join([str(x) for x in k['fingers']])
                    base_fret = k['baseFret']
                    position+= fmt3.format( frets, fingers , base_fret)+'\n'

                chord+= fmt2.format(j['key'], j['suffix'], position)+'\n'

            data+= fmt1.format(i, chord)

        with open('data.txt', 'w') as f2:
            f2.write(data)

    

process()