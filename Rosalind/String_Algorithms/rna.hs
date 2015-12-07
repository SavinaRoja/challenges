-- A solution to Rosalind Problem: RNA by SavinaRoja
-- http://rosalind.info/problems/rna/
-- Uses Data.ByteString to remove unnecessary overhead of string or Text
-- representation, and Data.ByteString.Lazy in particular for safety in
-- handling sequence files of arbitrary length.
--
-- This script is really quite trivial, it just replaces bytes of value 84 with
-- bytes of value 85, covnerting T to U in ASCII.

module Main where

import qualified Data.ByteString.Lazy as BL
import qualified Data.Map.Strict as M
import System.Environment

main :: IO ()
main = do
  args <- getArgs
  contents <- BL.readFile (head args)
  -- In ASCII: A = 65, C = 67, G = 71, T = 84, U = 85
  BL.putStr $ BL.pack [if x == 84 then 85 else x | x <- BL.unpack contents]


