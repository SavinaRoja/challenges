-- A solution to Rosalind Problem: HAMM by SavinaRoja
-- http://rosalind.info/problems/hamm/

module Main where

import Control.Applicative
import Control.Monad
import qualified Data.ByteString.Char8 as B
import System.Environment
import System.IO

hamming :: B.ByteString -> B.ByteString -> Integer
hamming s t = sum [1 | (x, y) <- B.zip s t , x /= y]

main :: IO ()
main = do
  args <- getArgs
  withFile (head args) ReadMode (\handle -> do 
    --More verbose form
    s <- B.hGetLine handle
    t <- B.hGetLine handle
    let hdist = hamming s t

    --Applicative forms
    --hdist <- liftA2 hamming (B.hGetLine handle) (B.hGetLine handle)
    --hdist <- hamming <$> (B.hGetLine handle) <*> (B.hGetLine handle)

    --Monadic form
    --hdist <- liftM2 hamming (B.hGetLine handle) (B.hGetLine handle)
    --hdist <- liftM2 hamming (B.hGetLine handle) (B.hGetLine handle)

    print hdist
    )
