import 'chord_library.dart';

void main() {
  // print(ChordLibrary.instrument(InstrumentType.guitar).getKeys());
  // print(ChordLibrary.guitar.getKeys());
  // for (var i in ChordLibrary.instrument(
  //   InstrumentType.ukulele,
  // ).getChordsByKey('C')!) {
  //   print(i.name);
  //   print(i.chordPositions);
  // }

  var instrument = ChordLibrary.instrument(InstrumentType.ukulele);

  var x = instrument.getChordPositions('C', 'major');
  print(x);
}
