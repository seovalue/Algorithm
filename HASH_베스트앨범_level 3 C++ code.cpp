#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;
vector<string> play_sum_of_genre; //장르별 곡 재생 횟수의 합
map<string, int> genre_play; //key 장르 val 플레이횟수
map<string, int> first_genre_pk;//실행횟수가 가장 큰 key 장르 val pk
map<string, int> second_genre_pk; //실행횟수가 두번째 큰 key 장르 val pk
map<string, int> m_count; //장르개수

bool isbigger(string a, string b){
    return genre_play[a] > genre_play[b];
    //장르명을 입력하면 재생횟수가 더 높으면 true를 반환
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;

    for(int i = 0; i < genres.size(); i++){
        int val = genre_play.find(genres[i])->second;
        if(val == genre_play.end()->second){
            //존재하지 않으면
            play_sum_of_genre.push_back(genres[i]);
            genre_play.insert(make_pair(genres[i],plays[i]));
            m_count[genres[i]] = 1;
        }
        else{
            genre_play[genres[i]] = val + plays[i];
            m_count[genres[i]] += 1;
        }

        int play1 = first_genre_pk.find(genres[i])->second;
        int play2 = second_genre_pk.find(genres[i])->second;

        if(play1 == first_genre_pk.end()->second){
            //first에 존재하지 않은 경우, 삽입
            first_genre_pk.insert(make_pair(genres[i],i));
        }
        else{
            //play1이 first에 pk로 존재하는 경우
            if(plays[play1] < plays[i]){
                //play1의 pk을 가진 노래보다 i의 pk를 가진 노래의 재생횟수가 클 때
                first_genre_pk[genres[i]] = i; //i로 대체
                second_genre_pk[genres[i]] = play1; //second에 play1을 넣음
            }
            else{
                //play1의 pk를 가진 노래가 재생횟수가 더 크면 first에 그대로 둠
                //play2 비교
                if(play2 == second_genre_pk.end()->second){
                    //second에 들어있지 않은 경우 삽입
                    second_genre_pk.insert(make_pair(genres[i],i));
                }
                else
                {//second에 존재
                    if(plays[play2] < plays[i]){
                        second_genre_pk[genres[i]] = i;
                    }
                }
            }
        }
    }

    //장르별 재생횟수 순으로 정렬
    sort(play_sum_of_genre.begin(),play_sum_of_genre.end(),isbigger);
    for(int i = 0; i < play_sum_of_genre.size(); i++){
        //first에 들어있는 값을 answer에 대입
        answer.push_back(first_genre_pk[play_sum_of_genre[i]]);
        if(m_count[play_sum_of_genre[i]] > 1)  //장르에 해당하는 곡이 1개 이상이면
            answer.push_back(second_genre_pk[play_sum_of_genre[i]]);
    }
    return answer;
}
