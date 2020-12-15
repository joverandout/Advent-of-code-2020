module Main where

import Control.Arrow ((&&&))
import qualified Data.Map as M
import Data.Map (Map)

type Plan = Map (Int, Int) Pos
type Input = Plan
data Pos = Floor | Empty | Taken deriving Show

prepare :: String -> Input
prepare input = M.fromList $ do
    (y, row) <- zip [0..] $ lines input
    (x, value) <- zip [0..] row
    pure ((y, x), parse value)
    where
        parse '.' = Floor
        parse 'L' = Empty
        parse '#' = Taken

partA = id

get :: IO String
get = readFile "seatingPlan.txt"

main :: IO ()
main = get >>= print . (partA) . prepare
