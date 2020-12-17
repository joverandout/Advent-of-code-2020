module Main where

import Lib
import Data.List.Split (splitOn)

import Data.IntMap (IntMap)
import qualified Data.IntMap.Strict as M

type Input = [Int]

data Game = Game {turns, lastTurn :: Int, saidMap :: IntMap Int}

findNextState :: Game -> Int
findNextState (Game ts mr sm) = case M.lookup mr sm of
                       Nothing -> 0
                       Just previous -> ts - previous

initial :: Input -> Game
initial inputs = Game (length inputs) (last inputs) . M.fromList . flip zip [1..] . init  $ inputs

step :: Game -> Game
step (Game ts mr sm) = Game (succ ts) (findNextState (Game ts mr sm)) $ M.insert mr ts sm

get :: IO String
get = readFile "input.txt"

main :: IO ()
main = do
       putStrLn "++++++++++++++++"
       putStr   "part 1: "
       get >>= print . (lastTurn . head . filter ((== 2020) . turns) . iterate step . initial) . (map read . splitOn ",")
       putStr   "part: 2 "
       get >>= print . (lastTurn . head . filter ((== 30000000) . turns) . iterate step . initial) . (map read . splitOn ",")
       putStrLn "++++++++++++++++"
