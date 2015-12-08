-- A solution to Rosalind Problem: REVC by SavinaRoja
-- http://rosalind.info/problems/revc/
-- Uses Data.ByteString to remove unnecessary overhead of string or Text
-- representation, and Data.ByteString.Lazy in particular for safety in
-- handling sequence files of arbitrary length.

module Main where

import Data.Word
import qualified Data.ByteString.Lazy as BL
import qualified Data.Map.Strict as M
import System.Environment

-- In ASCII: A = 65, C = 67, G = 71, T = 84
complement :: Word8 -> Word8
complement 65 = 84
complement 67 = 71
complement 71 = 67
complement 84 = 65
complement x = x  -- So we theoretically ignore any other unusual byte

main :: IO ()
main = do
  args <- getArgs
  contents <- BL.readFile (head args)

  -- One-liner below, but I broke it up a little here for clarity
  let revSeq = BL.unpack $ BL.reverse contents  -- Unpack the reverse bytestring
  let revComp = map complement revSeq         -- map complement to get reverse complement
  BL.putStr $ BL.pack revComp
  --BL.putStr $ BL.pack $ map complement $ BL.unpack $ BL.reverse contents

