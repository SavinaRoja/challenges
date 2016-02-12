import qualified Data.ByteString as B

class HammingDistanceable a where
  hamming :: (Eq a, Integral b) => a -> a -> b

instance (Eq a) => HammingDistanceable [a] where
  hamming s t = foldr (\(x,y) zs -> zs + if x == y then 0 else 1) 0 $ zip s t

instance HammingDistanceable (B.ByteString) where
  hamming s t = foldr (\(x,y) zs -> zs + if x == y then 0 else 1) 0 $ B.zip s t

--hamming :: (Eq a) => [a] -> [a] -> Integer
--hamming s t = sum [1 | (x, y) <- zip s t, x /= y]

--hamming2 :: (
