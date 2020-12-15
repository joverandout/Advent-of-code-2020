module Main where

import Control.Arrow ((&&&))
import qualified Data.Map as M
import Data.Map (Map)

type Plan = Map Doubly Pos
type Input = Plan
data Pos = Floor | Empty | Taken deriving (Eq, Show)
type Doubly = (Int, Int)

prepare :: String -> Input
prepare input = M.fromList $ do
    (y, row) <- zip [0..] $ lines input
    (x, value) <- zip [0..] row
    pure ((y, x), parse value)
    where
        parse '.' = Floor
        parse 'L' = Empty
        parse '#' = Taken

iterate :: Plan -> Doubly -> Pos -> Pos
iterate state doub p = case p of
    Floor -> Floor
    Empty | (length . filter (==Taken) . map (flip (M.findWithDefault Floor) state) . neighbouring $ doub) == 0 -> Taken
          | otherwise -> Empty
    Taken | (length . filter (==Taken) . map (flip (M.findWithDefault Floor) state) . neighbouring $ doub) >= 4 -> Empty
          | otherwise -> Taken

--length . filter (==Taken) . map (flip (M.findWithDefault Floor) state) . neighbors $ doub

first = id

get :: IO String
get = readFile "seatingPlan.txt"

main :: IO ()
main = get >>= print . (first) . prepare

neighbouring :: Doubly -> [Doubly]
neighbouring x = map (add x) . tail $ do
    dy <- [0,1,-1]
    dx <- [0,1,-1]
    pure (dy, dx)
    where add (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)
