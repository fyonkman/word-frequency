import unittest
import model

class modelUnitTests(unittest.TestCase):

    #tests that countWords creates a dictionary for a string of a single word
    def test_countWords_singleWord(self):
        self.assertEqual(model.countWords('hello'), {'hello': 1})

    #tests countWords correctly removes punctuation from strings
    def test_countWords_punctuationRemoval(self):
        self.assertEqual(model.countWords('!hello!'), {'hello': 1})

    #tests countWords removes all punctuation except apostrophes
    def test_countWords_apostrophe(self):
        self.assertEqual(model.countWords("!it's@"), {"it's": 1})

    #tests countWords correctly creates dictionary for multiple words
    def test_countWords_multipleWords(self):
        self.assertEqual(model.countWords('hello hello hello hi'),
                                            {'hello': 3, 'hi': 1})

    #tests countWords correctly creates dictionary for same word with
    #different capitalizations
    def test_countWords_multipleDiffCapitalization(self):
        self.assertEqual(model.countWords('hello Hello Hello'),
                                            {'hello': 3})

    #tests countWords orders dictionary by frequency in descending order                                    
    def test_countWords_descendingOrder(self):
        self.assertEqual(model.countWords('hi hi hello hello hello'),
                                            {'hello': 3, 'hi': 2})

    #the following unit tests test the STEM function for the
    #provided conjugated verb forms (talk, play, pass, and copy)
    def test_stem_talk(self):
        self.assertEqual(model.stem('talk'), 'talk')

    def test_stem_talks(self):
        self.assertEqual(model.stem('talks'), 'talk')

    def test_stem_talking(self):
        self.assertEqual(model.stem('talking'), 'talk')

    def test_stem_talked(self):
        self.assertEqual(model.stem('talked'), 'talk')

    def test_stem_play(self):
        self.assertEqual(model.stem('play'), 'play')

    def test_stem_plays(self):
        self.assertEqual(model.stem('plays'), 'play')

    def test_stem_playing(self):
        self.assertEqual(model.stem('playing'), 'play')

    def test_stem_played(self):
        self.assertEqual(model.stem('played'), 'play')

    def test_stem_pass(self):
        self.assertEqual(model.stem('pass'), 'pass')

    def test_stem_passes(self):
        self.assertEqual(model.stem('passes'), 'pass')

    def test_stem_passing(self):
        self.assertEqual(model.stem('passing'), 'pass')

    def test_stem_passed(self):
        self.assertEqual(model.stem('passed'), 'pass')

    def test_stem_copy(self):
        self.assertEqual(model.stem('copy'), 'copy')

    def test_stem_copies(self):
        self.assertEqual(model.stem('copies'), 'copy')

    def test_stem_copying(self):
        self.assertEqual(model.stem('copying'), 'copy')

    def test_stem_copied(self):
        self.assertEqual(model.stem('copied'), 'copy')

if __name__ == '__main__':
    unittest.main()
